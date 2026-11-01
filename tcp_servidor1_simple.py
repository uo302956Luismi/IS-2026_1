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

# Bucle principal de espera por clientes
while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)

    continuar = True

    # Bucle de atención al cliente conectado
    while continuar:
        datos = sd.recv(5)
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
