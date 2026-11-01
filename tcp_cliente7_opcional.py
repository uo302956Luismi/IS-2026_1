import socket
import sys
import struct

def recvall(sd, cantidad):
    buffer = []

    while cantidad > 0:
        datos = sd.recv(cantidad)

        if datos == b"":
            return b""

        buffer.append(datos)
        cantidad -= len(datos)

    return b"".join(buffer)


def recibe_mensaje(sd):
    longitud = recvall(sd, 2)

    if longitud == b"":
        return b""

    longitud = struct.unpack(">H", longitud)[0]

    return recvall(sd, longitud)


host = "localhost"
puerto = 9999

if len(sys.argv) >= 2:
    host = sys.argv[1]

if len(sys.argv) >= 3:
    puerto = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, puerto))

mensajes = ["UNO", "DOS", "TRES"]

for mensaje in mensajes:
    datos = mensaje.encode("utf8")
    longitud = struct.pack(">H", len(datos))

    s.sendall(longitud + datos)

for i in range(3):
    respuesta = recibe_mensaje(s)
    print(respuesta.decode("utf8"))

s.close()
exit(0)