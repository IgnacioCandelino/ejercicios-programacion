# Inicialización de variables
contador = 1
acumulador = 0

# Bucle while para recorrer del 1 al 10
while contador <= 10:
    if contador % 2 == 0:
        acumulador += contador
    contador += 1

# Mostrar el resultado
print(f"La suma de los números pares del 1 al 10 es: {acumulador}")
