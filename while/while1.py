# Inicialización de variables
contador = 1
acumulador = 0
maximo = 1
minimo = 1

# Bucle while para contar del 1 al 10
while contador <= 10:
    print(f"Número: {contador}")
    
    # Acumulador
    acumulador += contador

    # Máximo
    if contador > maximo:
        maximo = contador

    # Mínimo
    if contador < minimo:
        minimo = contador

    contador += 1

# Resultados
print(f"\nSuma total (acumulador): {acumulador}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
