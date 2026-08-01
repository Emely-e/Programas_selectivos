# Calculadora de calificaciones finales

def calcular_calificacion_final():
    parciales = float(input("Ingrese su calificación de los parciales (0-100): "))
    examen = float(input("Ingrese su calificación del examen (0-100): "))
    proyecto = float(input("Ingrese su calificación del proyecto (0-100): "))

    if not (0 <= parciales <= 100 and 0 <= examen <= 100 and 0 <= proyecto <= 100):
        print("Las calificaciones deben estar entre 0 y 100.")
        return None

    calificacion_final = (parciales * 0.4) + (examen * 0.4) + (proyecto * 0.2)

    if calificacion_final >= 90:
        letra = "A"
    elif calificacion_final >= 80:
        letra = "B"
    elif calificacion_final >= 70:
        letra = "C"
    elif calificacion_final >= 60:
        letra = "D"
    else:
        letra = "F"

    return letra, calificacion_final

resultado = calcular_calificacion_final()
if resultado is not None:
    letra, valor = resultado
    print(f"Calificación final: {letra} ({valor:.2f})")


