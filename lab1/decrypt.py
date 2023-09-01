import sys
import scapy.all as scapy

# Frecuencia de letras en español
spanish_letter_frequency = {
    'a': 11.96, 'b': 2.92, 'c': 4.92, 'd': 5.84, 'e': 13.59,
    'f': 0.69, 'g': 1.01, 'h': 0.7, 'i': 6.25, 'j': 0.44,
    'k': 0.01, 'l': 4.97, 'm': 3.15, 'n': 6.71, 'o': 8.68,
    'p': 2.51, 'q': 0.88, 'r': 6.87, 's': 7.98, 't': 4.63,
    'u': 3.93, 'v': 0.9, 'w': 0.01, 'x': 0.22, 'y': 0.9, 'z': 0.52
}

def decrypt_cesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Función para analizar los paquetes ICMP en el archivo pcapng
def analyze_icmp_packets(pcap_file):
    packets = scapy.rdpcap(pcap_file)  # Leer el archivo pcapng
    
    # Lista para almacenar los caracteres extraídos
    extracted_chars = []
    
    # Recorrer los paquetes y buscar ICMP requests hacia la dirección IP 8.8.8.8
    for packet in packets:
        if packet.haslayer(scapy.ICMP) and packet[scapy.ICMP].type == 8 and packet[scapy.IP].dst == "8.8.8.8":
            data = packet[scapy.Raw].load
            if data:
                first_char = chr(data[0])  # Convertir el primer byte en un caracter
                extracted_chars.append(first_char)
    
    return extracted_chars

if len(sys.argv) != 2:
    print("Uso: python programa.py archivo.pcapng")
    sys.exit(1)

# Ruta del archivo pcapng proporcionada como argumento
archivo_pcap = sys.argv[1]

# Obtener los caracteres extraídos de los paquetes ICMP
caracteres_extraidos = analyze_icmp_packets(archivo_pcap)

# Convertir los caracteres extraídos en una cadena
mensaje_cifrado = "".join(caracteres_extraidos)

# Imprimir el mensaje cifrado
print("Mensaje cifrado:", mensaje_cifrado)

# Inicializar variables para el mejor resultado
mejor_corrimiento = 0
mejor_mensaje = ""
mejor_puntaje = -1

# Realizar los corrimientos y mostrar todas las posibles combinaciones
for shift in range(26):
    decrypted_message = decrypt_cesar(mensaje_cifrado, shift)
    
    # Calcular el puntaje del mensaje usando la frecuencia de letras en español
    puntaje = sum(spanish_letter_frequency.get(char, 0) for char in decrypted_message.lower())
    
    # Actualizar el mejor mensaje si el puntaje es mayor
    if puntaje > mejor_puntaje:
        mejor_puntaje = puntaje
        mejor_corrimiento = shift
        mejor_mensaje = decrypted_message

# Imprimir el mensaje descifrado con el mejor corrimiento en verde
for shift in range(26):
    decrypted_message = decrypt_cesar(mensaje_cifrado, shift)
    if shift == mejor_corrimiento:
        print(f"Posible mensaje en claro con corrimiento {shift}: \033[32m{decrypted_message}\033[0m")
    else:
        print(f"Posible mensaje en claro con corrimiento {shift}: {decrypted_message}")

