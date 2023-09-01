import random
import sys
from scapy.all import *

def enviar_paquete_icmp(mensaje):
    # Convierte el mensaje en una lista de caracteres
    caracteres = list(mensaje)

    # Genera un identificador aleatorio de 16 bits
    identificador = random.randint(0, 65535)

    # Inicializa el número de secuencia
    secuencia = 1

    # Itera sobre cada carácter y envía un paquete ICMP
    for char in caracteres:
        # Convierte el carácter en bytes
        char_byte = bytes(char, 'utf-8')

        # Crea el paquete ICMP con el carácter y el relleno
        paquete_icmp = IP(dst="8.8.8.8", ttl=64) / ICMP(type=8, id=identificador, seq=secuencia) / Raw(load=char_byte + bytes.fromhex("00000000000000101112131415161718191a1b1c1e1d1f202122232425262728292a2b2c2d2e2f3031323334353637"))

        # Envía el paquete ICMP
        send(paquete_icmp, verbose=False)

        # Incrementa el número de secuencia
        secuencia += 1

    # Muestra la cantidad total de paquetes enviados
    print(f"Total de paquetes enviados: {len(caracteres)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python programa.py \"mensaje a enviar\"")
    else:
        mensaje = sys.argv[1]
        enviar_paquete_icmp(mensaje)
