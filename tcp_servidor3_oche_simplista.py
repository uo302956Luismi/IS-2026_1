import socket
import sys

puerto = 9999

if len(sys.argv) >= 2:
    puerto = int(sys.argv[1])

# Creación del socket de escucha
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asignarle puerto
s.bind(("", puerto))

# Ponerlo en modo pasivo
s.listen(5)

while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)

    continuar = True

    while continuar:
        mensaje = sd.recv(80)

        if mensaje == b"":
            sd.close()
            continuar = False

        else:
            mensaje = mensaje.decode("utf8")

            linea = mensaje[:-2]
            linea = linea[::-1]

            sd.sendall(bytes(linea + "\r\n", "utf8"))
