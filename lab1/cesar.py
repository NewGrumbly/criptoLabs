import sys

def cifrado_cesar(texto, corrimiento):
    texto_cifrado = ""

    for caracter in texto:
        if caracter.isalpha():  # Verificamos si el caracter es una letra
            if caracter.islower():  # Si es minúscula
                nuevo_valor = (ord(caracter) - ord('a') + corrimiento) % 26 + ord('a')
                texto_cifrado += chr(nuevo_valor)
            elif caracter.isupper():  # Si es mayúscula
                nuevo_valor = (ord(caracter) - ord('A') + corrimiento) % 26 + ord('A')
                texto_cifrado += chr(nuevo_valor)
        else:
            texto_cifrado += caracter  # Mantenemos caracteres no alfabéticos sin cambios

    return texto_cifrado

# Verificamos si se proporcionaron los argumentos correctos
if len(sys.argv) != 3:
    print("Uso: python programa.py <texto a cifrar> <corrimiento>")
    sys.exit(1)

# Obtenemos los argumentos de la línea de comandos
texto_original = sys.argv[1]
corrimiento = int(sys.argv[2])

# Aplicamos el cifrado César y mostramos el resultado
texto_cifrado = cifrado_cesar(texto_original, corrimiento)
print("Texto cifrado:", texto_cifrado)

