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

for i in range(5):
    s.sendall("ABCDE".encode("ascii"))

s.sendall("FINAL".encode("ascii"))

s.close()
exit(0)
