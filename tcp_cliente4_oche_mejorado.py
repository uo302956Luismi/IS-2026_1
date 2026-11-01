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
    s.sendall(bytes(mensaje + "\r\n", "utf8"))

for i in range(3):
    respuesta = recibe_mensaje(s)
    print(repr(respuesta.decode("utf8")))

s.close()
exit(0)