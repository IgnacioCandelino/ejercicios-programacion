# Inicialización de variables
suma = 0
contador = 0

# Bucle while para ingresar al menos 5 números
while contador < 5:
    numero = float(input("Ingrese un número: "))
    suma += numero
    contador += 1

# Calcular el promedio
promedio = suma / contador

# Mostrar los resultados
print(f"\nLa suma de los números ingresados es: {suma}")
print(f"El promedio de los números ingresados es: {promedio}")
