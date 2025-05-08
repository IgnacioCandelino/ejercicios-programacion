# Inicialización de variables
suma_positivos = 0
suma_negativos = 0
contador_positivos = 0
contador_negativos = 0
maximo_positivo = 0
total_numeros = 0

# Bucle while para ingresar números
continuar = 'sí'
while continuar == 'sí':
    numero = float(input("Ingrese un número: "))
    
    # Sumar y contar números según si son positivos o negativos
    if numero > 0:
        suma_positivos += numero
        contador_positivos += 1
        if numero > maximo_positivo:
            maximo_positivo = numero
    elif numero < 0:
        suma_negativos += numero
        contador_negativos += 1
    
    total_numeros += 1
    
    # Preguntar si desea continuar ingresando números
    continuar = input("¿Desea ingresar otro número? (sí/no): ").strip().lower()

# Calcular el promedio de los números positivos
if contador_positivos > 0:
    promedio_positivos = suma_positivos / contador_positivos
else:
    promedio_positivos = 0

# Calcular el porcentaje de números negativos respecto al total
if total_numeros > 0:
    porcentaje_negativos = (contador_negativos / total_numeros) * 100
else:
    porcentaje_negativos = 0

# Mostrar los resultados
print(f"\nSuma acumulada de los números positivos: {suma_positivos}")
print(f"Suma acumulada de los números negativos: {suma_negativos}")
print(f"Cantidad de números negativos ingresados: {contador_negativos}")
print(f"Promedio de los números positivos: {promedio_positivos}")
print(f"Número positivo más grande: {maximo_positivo}")
print(f"Porcentaje de números negativos ingresados: {porcentaje_negativos:.2f}%")
