# Ingreso de la altura del jugador
altura = int(input("Ingrese la altura del jugador en centímetros: "))

# Determinación de la posición según la altura
if altura < 160:
    posicion = "Base"
elif 160 <= altura <= 179:
    posicion = "Escolta"
elif 180 <= altura <= 199:
    posicion = "Alero"
else:
    posicion = "Ala-Pívot o Pívot"

print(f"La posición del jugador es: {posicion}")
