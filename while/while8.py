# Inicialización de variables
maximo = 0
minimo = 0
contador = 1

# Bucle while para ingresar 10 números
while contador <= 10:
    numero = int(input(f"Ingrese el número {contador}: "))
    
    # En la primera iteración, asignamos el número como máximo y mínimo
    if contador == 1:
        maximo = numero
        minimo = numero
    else:
        # Determinar el máximo y mínimo
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    
    contador += 1

# Mostrar los resultados
print(f"\nEl número máximo ingresado es: {maximo}")
print(f"El número mínimo ingresado es: {minimo}")
