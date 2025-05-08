# Inicializar la nota como un valor fuera del rango válido
nota = 0

# Bucle while para validar que la nota esté entre 1 y 10
while nota < 1 or nota > 10:
    nota = float(input("Por favor, ingrese una nota entre 1 y 10: "))
    
    # Verificar si la nota está en el rango válido
    if nota < 1 or nota > 10:
        print("La nota debe estar entre 1 y 10. Intente nuevamente.")
    else:
        print(f"Nota válida: {nota}")
