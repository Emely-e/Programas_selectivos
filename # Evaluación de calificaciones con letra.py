# Evaluación de calificaciones con letras
nota = float(input("Ingresa tu calificación (0-100): "))

if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
else:
    letra = "F"

match letra:
    case "A":
        print("Excelente")
    case "B":
        print("Muy bien")
    case "C":
        print("Bien")
    case "D":
        print("Suficiente")
    case "F":
        print("Insuficiente")
