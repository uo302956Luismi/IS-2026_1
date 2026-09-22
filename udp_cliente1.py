import socket
import sys

if len(sys.argv) < 3:
    print("El numero de parametros es incorrecto, ha de ser ./programa ip puerto")
    exit(1)

host = sys.argv[1]
puerto = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
linea = ""
while linea != "FIN":
    linea = input("Ponga su texto, ingrese 'FIN' para cerrar")
    s.sendto(linea.encode("utf8"), (host,puerto))

exit(0)