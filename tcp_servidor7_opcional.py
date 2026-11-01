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


puerto = 9999

if len(sys.argv) >= 2:
    puerto = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)

while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)

    continuar = True

    while continuar:
        mensaje = recibe_mensaje(sd)

        if mensaje == b"":
            sd.close()
            continuar = False

        else:
            linea = mensaje.decode("utf8")
            linea = linea[::-1]

            respuesta = linea.encode("utf8")
            longitud = struct.pack(">H", len(respuesta))

            sd.sendall(longitud + respuesta)