import socket
import sys

host = "localhost"
puerto = 9999

if len(sys.argv) >= 2:
    host = sys.argv[1]

if len(sys.argv) >= 3:
    puerto = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, puerto))

f = s.makefile(encoding="utf8", newline="\r\n")

mensajes = ["UNO", "DOS", "TRES"]

for mensaje in mensajes:
    s.sendall(bytes(mensaje + "\r\n", "utf8"))

for i in range(3):
    respuesta = f.readline()
    print(repr(respuesta))

f.close()
s.close()
exit(0)