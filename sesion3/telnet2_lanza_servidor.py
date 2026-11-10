import telnetlib
import getpass
import sys

# Servidor remoto: por defecto localhost.
# También se puede indicar la IP al ejecutar el programa.
HOST = sys.argv[1] if len(sys.argv) > 1 else "localhost"
PORT = 23

usuario = input("Usuario remoto: ")
clave = getpass.getpass("Contraseña remota: ")

try:
    print(f"\nConectando por Telnet a {HOST}...")

    tn = telnetlib.Telnet(HOST, PORT, timeout=10)

    # Esperar a que el servidor solicite el usuario.
    tn.read_until(b"login:", timeout=10)
    tn.write(usuario.encode("utf-8") + b"\n")

    # Esperar a que solicite la contraseña.
    tn.read_until(b"Password:", timeout=10)
    tn.write(clave.encode("utf-8") + b"\n")

    # Esperar al prompt del shell.
    tn.read_until(b"$", timeout=10)

    print("Conexión establecida correctamente.")

    # Consultar el estado del servicio SSH.
    tn.write(b"systemctl is-active ssh\n")

    respuesta = tn.read_until(b"$", timeout=10)
    texto = respuesta.decode("utf-8", errors="replace")

    # Mostrar el estado encontrado.
    estado = None
    for linea in texto.splitlines():
        linea = linea.strip()
        if linea in ("active", "inactive", "failed", "activating", "deactivating"):
            estado = linea
            break

    if estado:
        print("\nEstado del servicio SSH:", estado)
        if estado == "active":
            print("El servicio SSH está en ejecución.")
        else:
            print("El servicio SSH no está en ejecución.")
    else:
        print("\nNo se ha podido identificar el estado.")
        print("Respuesta recibida:")
        print(texto)

    # Cerrar la sesión remota.
    tn.write(b"exit\n")
    print("\nCerrando conexión Telnet...")

    tn.read_all()
    tn.close()

    print("Conexión cerrada.")

except Exception as e:
    print("\nError durante la conexión Telnet:", e)
