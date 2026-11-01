
import socket
import sys

if len(sys.argv) < 2:
    print("Uso: ./programa ip_broadcast")
    exit(1)

broadcast = sys.argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto("BUSCANDO HOLA".encode("utf8"), (broadcast, 12345))
s.settimeout(2)
primero = None

while True:
    try:
        datagrama, origen = s.recvfrom(1024)
        mensaje = datagrama.decode("utf8")
        if mensaje == "IMPLEMENTO HOLA":
            print("Servidor encontrado:", origen[0])
            if primero is None:
                primero = origen[0]
    except socket.timeout:
        break
if primero is not None:
    s.sendto("HOLA".encode("utf8"), (primero, 12345))
    datagrama, origen = s.recvfrom(1024)
    print("Respuesta del servidor:")
    print(datagrama.decode("utf8"))
else:
    print("No se ha encontrado ningun servidor HOLA")
s.close()
exit(0)
