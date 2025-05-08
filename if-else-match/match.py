estacion = input("Ingrese la estación del año (invierno, verano, otoño, primavera): ").lower()
destino = input("Ingrese el destino (Bariloche, Mar del plata, Cataratas): ").lower()


match estacion:
    case "invierno":
        if destino == "bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case "verano":
        if destino in ["mar del plata", "cataratas"]:
            print("Se viaja")
        else:
            print("No se viaja")
    case "otoño":
        print("Se viaja")
    case "primavera":
        if destino == "bariloche":
            print("No se viaja")
        else:
            print("Se viaja")
    case _:
        print("Estación no válida")
