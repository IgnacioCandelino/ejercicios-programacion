# Inicialización de variables
suma = 0
contador = 0

# Solicitar la cantidad de números entre 5 y 10
while contador < 5 or contador > 10:
    cantidad = int(input("¿Cuántos números desea ingresar (mínimo 5 y máximo 10)? "))
    if cantidad < 5 or cantidad > 10:
        print("Debe ingresar entre 5 y 10 números. Intente nuevamente.")

# Bucle while para ingresar los números
while contador < cantidad:
    numero = float(input(f"Ingrese el número {contador + 1}: "))
    suma += numero
    contador += 1

# Calcular el promedio
promedio = suma / cantidad

# Mostrar los resultados
print(f"\nLa suma de los números ingresados es: {suma}")
print(f"El promedio de los números ingresados es: {promedio}")
