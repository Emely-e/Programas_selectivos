# Verificar edad para votar

def verificar_edad(edad):
    if edad >= 18:
        return "Puedes votar"
    else:
        return "No puedes votar"

edad = int(input("Ingresa tu edad: "))
resultado = verificar_edad(edad)
print(resultado)
