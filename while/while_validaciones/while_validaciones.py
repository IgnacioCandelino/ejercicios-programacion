# Definir la clave correcta
clave_correcta = "secreta"

# Bucle while para pedir la clave hasta que sea correcta
while True:
    clave_ingresada = input("Por favor, ingrese la clave: ")
    
    # Verificar si la clave ingresada es correcta
    if clave_ingresada == clave_correcta:
        print("Clave correcta. Acceso concedido.")
        break
    else:
        print("Clave incorrecta. Intente nuevamente.")
