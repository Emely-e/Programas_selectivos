celsius = float(input("Ingresa el grado en Celsius: "))
opcion = input("Convierte a Fahrenheit (F) o Kelvin (K): ").strip().upper()

# if-elif-else para elegir la conversión
if opcion == "F":
    resultado = celsius * 9 / 5 + 32
    unidad = "Fahrenheit"
elif opcion == "K":
    resultado = celsius + 273.15
    unidad = "Kelvin"
else:
    resultado = None
    unidad = None

if resultado is None:
    print("Opción inválida. Escribe F o K.")
else:
    print(f"{celsius:.1f} °C son {resultado:.2f} °{unidad[0]} ({unidad})")

# match-case para mostrar el mensaje final según la opción
match opcion:
    case "F":
        print("match-case: Convertido a Fahrenheit")
    case "K":
        print("match-case: Convertido a Kelvin")
    case _:
        print("match-case: Opción inválida")