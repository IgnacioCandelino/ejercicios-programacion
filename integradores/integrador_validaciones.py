# Solicitar y validar el apellido
apellido = input("Ingrese su apellido: ")

# Solicitar y validar la edad
edad = 0
while edad < 18 or edad > 90:
    edad = int(input("Ingrese su edad (entre 18 y 90 años inclusive): "))
    if edad < 18 or edad > 90:
        print("Edad inválida. Debe estar entre 18 y 90 años.")

# Solicitar y validar el estado civil
estado_civil = ""
while estado_civil != "Soltero/a" and estado_civil != "Casado/a" and estado_civil != "Divorciado/a" and estado_civil != "Viudo/a":
    estado_civil = input("Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a): ")
    if estado_civil != "Soltero/a" and estado_civil != "Casado/a" and estado_civil != "Divorciado/a" and estado_civil != "Viudo/a":
        print("Estado civil inválido. Debe ser uno de los siguientes: Soltero/a, Casado/a, Divorciado/a, Viudo/a.")

# Solicitar y validar el número de legajo
legajo = 0
while legajo < 1000 or legajo > 9999:
    legajo = int(input("Ingrese su número de legajo (valor numérico de 4 cifras): "))
    if legajo < 1000 or legajo > 9999:
        print("Número de legajo inválido. Debe ser un número de 4 cifras sin ceros a la izquierda.")

# Mostrar los datos ingresados
print("\nDatos ingresados:")
print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado Civil: {estado_civil}")
print(f"Número de Legajo: {legajo}")
