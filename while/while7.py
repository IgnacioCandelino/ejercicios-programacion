# Inicialización de variables
suma_positivos = 0
producto_negativos = 1
hay_negativos = False  # Para verificar si hubo números negativos

# Bucle para ingresar números hasta que el usuario decida detenerse
while True:
    numero = float(input("Ingrese un número (o escriba 'fin' para terminar): "))
    
    if numero > 0:
        suma_positivos += numero
    elif numero < 0:
        producto_negativos *= numero
        hay_negativos = True

    continuar = input("¿Desea ingresar otro número? (sí/no): ").strip().lower()
    if continuar != 'sí':
        break

# Mostrar los resultados
print(f"\nLa suma de los números positivos es: {suma_positivos}")
if hay_negativos:
    print(f"El producto de los números negativos es: {producto_negativos}")
else:
    print("No se ingresaron números negativos.")
