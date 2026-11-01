import socket
import sys

def recibe_mensaje(f):
    longitud = f.readline()

    if longitud == b"":
        return b""

    longitud = int(longitud.decode("ascii"))

    mensaje = f.read(longitud)

    return mensaje


host = "localhost"
puerto = 9999

if len(sys.argv) >= 2:
    host = sys.argv[1]

if len(sys.argv) >= 3:
    puerto = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, puerto))

f = s.makefile("rb")

mensajes = ["UNO", "DOS", "TRES"]

for mensaje in mensajes:
    datos = mensaje.encode("utf8")
    longitud = str(len(datos)).encode("ascii") + b"\n"

    s.sendall(longitud + datos)

for i in range(3):
    respuesta = recibe_mensaje(f)
    print(respuesta.decode("utf8"))

f.close()
s.close()
exit(0)