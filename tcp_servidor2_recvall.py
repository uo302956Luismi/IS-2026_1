import socket
import sys

def recvall(sd, cantidad):
    buffer = []

    while cantidad > 0:
        datos = sd.recv(cantidad)

        if datos == b"":
            return b""

        buffer.append(datos)
        cantidad -= len(datos)

    return b"".join(buffer)


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
        datos = recvall(sd, 5)
        datos = datos.decode("ascii")

        if datos == "":
            print("Conexion cerrada de forma inesperada por el cliente")
            sd.close()
            continuar = False

        elif datos == "FINAL":
            print("Recibido mensaje de finalizacion")
            sd.close()
            continuar = False

        else:
            print("Recibido mensaje: %s" % datos)
