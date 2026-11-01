import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(("", 12345))

while True:
    datagrama, origen = s.recvfrom(1024)
    mensaje = datagrama.decode("utf8")

    if mensaje == "BUSCANDO HOLA":
        respuesta = "IMPLEMENTO HOLA"
        s.sendto(respuesta.encode("utf8"), origen)
    elif mensaje == "HOLA":
        respuesta = f"HOLA: {origen[0]}"
        s.sendto(respuesta.encode("utf8"), origen)
