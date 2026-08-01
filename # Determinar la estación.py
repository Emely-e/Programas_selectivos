# Determinar la estación
mes = int(input("Ingresa el mes (1-12): "))

if 3 <= mes <= 5:
    estacion = "Primavera"
elif 6 <= mes <= 8:
    estacion = "Verano"
elif 9 <= mes <= 11:
    estacion = "Otoño"
elif mes == 12 or mes == 1 or mes == 2:
    estacion = "Invierno"
else:
    estacion = "Mes inválido"

print(f"Estación según if-elif-else: {estacion}")

match mes:
    case 3 | 4 | 5:
        print("match-case: Primavera")
    case 6 | 7 | 8:
        print("match-case: Verano")
    case 9 | 10 | 11:
        print("match-case: Otoño")
    case 12 | 1 | 2:
        print("match-case: Invierno")
    case _:
        print("match-case: Mes inválido")
