import socket
import sys

def recibe_mensaje(f):
    longitud = f.readline()

    if longitud == b"":
        return b""

    longitud = int(longitud.decode("ascii"))

    mensaje = f.read(longitud)

    return mensaje


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

    f = sd.makefile("rb")

    continuar = True

    while continuar:
        mensaje = recibe_mensaje(f)

        if mensaje == b"":
            f.close()
            sd.close()
            continuar = False

        else:
            linea = mensaje.decode("utf8")
            linea = linea[::-1]

            respuesta = linea.encode("utf8")
            longitud = str(len(respuesta)).encode("ascii") + b"\n"

            sd.sendall(longitud + respuesta)