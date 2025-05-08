# Inicialización de variables
acumulador = 0
contador = 0

# Bucle para ingresar números hasta que el usuario decida detenerse
while True:
    numero = float(input("Ingrese un número (o escriba 'fin' para terminar): "))
    acumulador += numero
    contador += 1
    
    continuar = input("¿Desea ingresar otro número? (sí/no): ").strip().lower()
    if continuar != 'sí':
        break

# Cálculo del promedio
if contador > 0:
    promedio = acumulador / contador
    # Mostrar resultados
    print(f"\nLa suma de los números es: {acumulador}")
    print(f"El promedio es: {promedio}")
else:
    print("No se ingresaron números.")
