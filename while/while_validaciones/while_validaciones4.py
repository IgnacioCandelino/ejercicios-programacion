# Bucle while para validar que el color sea Rojo, Verde o Azul
color = ""

while color != "Rojo" and color != "Verde" and color != "Azul":
    color = input("Por favor, ingrese un color (Rojo, Verde o Azul): ")

    # Validar que el color ingresado sea uno de los tres colores válidos
    if color != "Rojo" and color != "Verde" and color != "Azul":
        print("Color inválido. Debe ser Rojo, Verde o Azul. Intente nuevamente.")
    else:
        print(f"Color válido: {color}")
