
import socket
import sys

if len(sys.argv) < 3:
    print("El numero de parametros es incorrecto, ha de ser ./programa ip puerto")
    exit(1)

host = sys.argv[1]
puerto = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((host, puerto))
contador = 1
linea = ""

while linea != "FIN":
    linea = input("Ponga su texto, ingrese 'FIN' para cerrar: ")
    if linea == "FIN":
        break
    mensaje = f"{contador}: {linea}"
    recib = False
    timeout = 0.1

    while not recib:
        s.settimeout(timeout)
        try:
            s.send(mensaje.encode("utf8"))
            datagrama = s.recv(1024).decode("utf8")
            print("Contiene lo siguiente:")
            print(datagrama)
            if datagrama == f"OK {contador}":
                recib = True
        except socket.timeout:
            print("ERROR: El OK del server no llego")
            timeout *= 2
            if timeout > 2:
                print("Puede que el servidor este caido")
                s.close()
                exit(1)
    contador += 1
s.close()
exit(0)
