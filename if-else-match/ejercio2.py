import random

# Generar una nota aleatoria entre 1 y 10
nota = random.randint(1, 10)

# Evaluación según la nota
if nota >= 6:
    print(f"Promoción directa, la nota es {nota}")
elif nota >= 4:
    print(f"Aprobado, la nota es {nota}")
else:
    print(f"Desaprobado, la nota es {nota}")
