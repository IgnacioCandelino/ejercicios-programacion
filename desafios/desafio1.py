# Entrada de datos
consumo = float(input("Ingrese la cantidad de metros cúbicos consumidos: "))
tipo_cliente = input("Ingrese el tipo de cliente (Residencial, Comercial o Industrial): ").strip().lower()

# Valores fijos
cargo_fijo = 7000
precio_m3 = 200
subtotal_consumo = consumo * precio_m3
subtotal_sin_ajustes = subtotal_consumo + cargo_fijo

# Inicialización de variables
bonificacion = 0
recargo = 0
descuento_especial = 0

# Lógica de bonificaciones y recargos según tipo de cliente
if tipo_cliente == "residencial":
    if consumo < 30:
        bonificacion = 0.10 * subtotal_consumo
    elif consumo > 80:
        recargo = 0.15 * subtotal_consumo
    
    # Descuento especial
    if subtotal_sin_ajustes < 35000:
        descuento_especial = 0.05 * subtotal_sin_ajustes

elif tipo_cliente == "comercial":
    if consumo > 300:
        bonificacion = 0.12 * subtotal_consumo
    elif consumo > 150:
        bonificacion = 0.08 * subtotal_consumo
    elif consumo < 50:
        recargo = 0.05 * subtotal_consumo

elif tipo_cliente == "industrial":
    if consumo > 1000:
        bonificacion = 0.30 * subtotal_consumo
    elif consumo > 500:
        bonificacion = 0.20 * subtotal_consumo
    elif consumo < 200:
        recargo = 0.10 * subtotal_consumo
else:
    print("Tipo de cliente no válido.")
    exit()

# Cálculo del subtotal con ajustes
subtotal_ajustado = subtotal_sin_ajustes + recargo - bonificacion - descuento_especial

# IVA
iva = 0.21 * subtotal_ajustado

# Total final
total_final = subtotal_ajustado + iva

# Desglose
print("\n--- FACTURA DEL SERVICIO DE AGUA POTABLE ---")
print(f"Consumo registrado: {consumo} m³")
print(f"Tipo de cliente: {tipo_cliente.capitalize()}")
print(f"Cargo fijo: ${cargo_fijo:.2f}")
print(f"Costo por consumo: ${subtotal_consumo:.2f}")
print(f"Bonificación aplicada: ${bonificacion:.2f}")
print(f"Recargo aplicado: ${recargo:.2f}")
print(f"Descuento especial: ${descuento_especial:.2f}")
print(f"Subtotal con ajustes: ${subtotal_ajustado:.2f}")
print(f"IVA (21%): ${iva:.2f}")
print(f"TOTAL A PAGAR: ${total_final:.2f}")
