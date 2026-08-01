# Conversor de monedas
pesos = float(input("Ingresa la cantidad en pesos mexicanos (MXN): "))
moneda = input(
    "Elige la moneda destino (USD, EUR, THB, JPY, KRW, AUD, PEN, CAD, VES, ARS): "
).strip().upper()

# Tasas de conversión aproximadas
if moneda == "USD":
    tasa = 0.056
elif moneda == "EUR":
    tasa = 0.052
elif moneda == "THB":
    tasa = 1.90
elif moneda == "JPY":
    tasa = 8.50
elif moneda == "KRW":
    tasa = 73.50
elif moneda == "AUD":
    tasa = 0.084
elif moneda == "PEN":
    tasa = 0.21
elif moneda == "CAD":
    tasa = 0.075
elif moneda == "VES":
    tasa = 0.00026
elif moneda == "ARS":
    tasa = 4.70
else:
    tasa = None

if tasa is None:
    print("Moneda inválida. Ingresa uno de los códigos permitidos.")
else:
    convertido = pesos * tasa
    print(f"{pesos:.2f} MXN son {convertido:.2f} {moneda}")

match moneda:
    case "USD":
        print("match-case: Convertido a dólares estadounidenses")
    case "EUR":
        print("match-case: Convertido a euros")
    case "THB":
        print("match-case: Convertido a bahts tailandeses")
    case "JPY":
        print("match-case: Convertido a yenes japoneses")
    case "KRW":
        print("match-case: Convertido a wones surcoreanos")
    case "AUD":
        print("match-case: Convertido a dólares australianos")
    case "PEN":
        print("match-case: Convertido a soles peruanos")
    case "CAD":
        print("match-case: Convertido a dólares canadienses")
    case "VES":
        print("match-case: Convertido a bolívares venezolanos")
    case "ARS":
        print("match-case: Convertido a pesos argentinos")
    case _:
        print("match-case: Moneda inválida")
        