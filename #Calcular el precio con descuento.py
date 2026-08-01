#Calcular el precio con descuento
precio = float(input("Ingrese el precio original: "))

if precio <= 100:
    descuento = 0.05
elif precio <= 200:
    descuento = 0.10
elif precio <= 500:
    descuento = 0.15
else:
    descuento = 0.20

precio_final = precio * (1 - descuento)
print(f"Descuento: {descuento*100:.0f}%")
print(f"Precio con descuento: {precio_final:.2f}")

# match-case usando el rango de descuento calculado
match descuento:
    case 0.05:
        print("Rango: hasta 100")
    case 0.10:
        print("Rango: hasta 200")
    case 0.15:
        print("Rango: hasta 500")
    case 0.20:
        print("Rango: más de 500")
    case _:
        print("Rango desconocido")
