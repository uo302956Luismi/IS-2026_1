import socket
import sys

if len(sys.argv) < 3:
    print("El numero de parametros es incorrecto, ha de ser ./programa puerto")
    exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", int(sys.argv[1])))

datagrama, origen = s.revfrom(1024)  # 1024 es el máximo tamaño esperado
print("Se ha recibido un datagrama desde", origen)
print("Contiene lo siguiente:")
print(datagrama.decode("utf-8"))
# Ahora lo devolvemos a modo de eco
s.sendto(datagrama, origen)

exit(0)