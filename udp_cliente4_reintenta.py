import socket
import sys

if len(sys.argv) < 3:
    print("El numero de parametros es incorrecto, ha de ser ./programa ip puerto")
    exit(1)

host = sys.argv[1]
puerto = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

contador = 1

while linea != "FIN":
    linea = input("Ponga su texto, ingrese 'FIN' para cerrar: ")
    mensaje = f"{contador}: {linea}"
    recib = False
    while not recib:
        s.sendto(mensaje.encode("utf8"), (host,puerto))
        s.settimeout(0.1)
        datagrama, origen = s.recvfrom(1024)  # 1024 es el máximo tamaño esperado
        
        try:
            s.sendto(mensaje.encode("utf8"), (host,puerto))
            datagrama, origen = s.recvfrom(1024)  # 1024 es el máximo tamaño esperado
            print("Se ha recibido un datagrama desde", origen)
            print("Contiene lo siguiente:")
            print(datagrama.decode("utf-8"))
            if datagrama.decode("utf-8") == "OK":
                recib = True
                contador += 1
        except socket.timeout:
            print("ERROR: El Ok del server no llego")

exit(0)