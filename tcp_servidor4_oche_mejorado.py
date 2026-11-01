import socket
import sys

def recibe_mensaje(sd):
    buffer = []

    while True:
        byte = sd.recv(1)

        if byte == b"":
            return b""

        buffer.append(byte)

        if len(buffer) >= 2 and buffer[-2] == b"\r" and buffer[-1] == b"\n":
            return b"".join(buffer)


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
            mensaje = mensaje.decode("utf8")

            linea = mensaje[:-2]
            linea = linea[::-1]

            sd.sendall(bytes(linea + "\r\n", "utf8"))
