# Abre el archivo RockYou original y el archivo de salida para el diccionario modificado
with open('rockyou.txt', 'rb') as file, open('rockyou_mod.dic', 'w', encoding='utf-8', errors='ignore') as output_file:
    modified_passwords = []  # Lista para almacenar las contraseñas modificadas

    # Recorre el archivo línea por línea
    for line in file:
        try:
            password = line.decode('utf-8').strip()  # Decodifica la línea como UTF-8 y elimina espacios
                                                    #en blanco y saltos de línea

            # Comprueba si la línea no está vacía y si no comienza con un número
            if password and not password[0].isdigit():
                # Capitaliza la primera letra y agrega '0' al final
                modified_password = password[0].upper() + password[1:] + '0'
                modified_passwords.append(modified_password)
        except UnicodeDecodeError:
            continue  # Ignora caracteres no válidos y continúa con la siguiente línea
    
    # Escribe las contraseñas modificadas en el archivo de salida
    output_file.write('\n'.join(modified_passwords))

# Imprime la cantidad de contraseñas en el diccionario modificado
print(f"La cantidad de contraseñas en el diccionario modificado es: {len(modified_passwords)}")

