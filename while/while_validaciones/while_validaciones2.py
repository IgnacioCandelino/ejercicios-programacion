# Definir la clave correcta
clave_correcta = "secreta"

# Inicializar el contador de intentos
intentos = 0
max_intentos = 3

# Bucle while para pedir la clave hasta que sea correcta o se agoten los intentos
while intentos < max_intentos:
    clave_ingresada = input("Por favor, ingrese la clave: ")
    
    # Verificar si la clave ingresada es correcta
    if clave_ingresada == clave_correcta:
        print("Clave correcta. Acceso concedido.")
        # Se termina el bucle sin usar break
        intentos = max_intentos  # Salir del bucle al cambiar el contador
    else:
        intentos += 1
        if intentos < max_intentos:
            print(f"Clave incorrecta. Te quedan {max_intentos - intentos} intentos.")
        else:
            print("Has agotado tus 3 intentos. Acceso denegado.")
