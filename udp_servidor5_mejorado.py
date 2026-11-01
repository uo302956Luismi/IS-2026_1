import socket
import sys
import random

puerto = 9999

if len(sys.argv) >= 2:
    puerto = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", puerto))
recibidos = set()

while True:
    datagrama, origen = s.recvfrom(1024)
    mensaje = datagrama.decode("utf8")
    numero, texto = mensaje.split(": ", 1)
    if numero not in recibidos:
        print("Se ha recibido un datagrama desde", origen)
        print("Contiene lo siguiente:")
        print(mensaje)
        recibidos.add(numero)
    else:
        print("Datagrama duplicado:", numero)
    respuesta = f"OK {numero}"
    s.sendto(respuesta.encode("utf8"), origen)
