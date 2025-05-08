# Inicialización de variables
contador = 1
acumulador = 0

# Bucle para pedir 5 números
while contador <= 5:
    numero = float(input(f"Ingrese el número {contador}: "))
    acumulador += numero
    contador += 1

# Cálculo del promedio
promedio = acumulador / 5

# Mostrar resultados
print(f"\nLa suma de los números es: {acumulador}")
print(f"El promedio es: {promedio}")
