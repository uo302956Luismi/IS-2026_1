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

mensajes = ["HOLA", "MUNDO", "PYTHON"]

for mensaje in mensajes:
    s.sendall(bytes(mensaje + "\r\n", "utf8"))

    respuesta = s.recv(80)
    print(respuesta.decode("utf8"))

s.close()
exit(0)
