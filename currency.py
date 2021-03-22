menu = """
Bienvenido al conversor de monedas 🤗

1 - Pesos mexicanos
2 - Pesos colombianos
3 - Pesos argentinos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Peso mexicano: ")
    pesos = float(pesos)
    valor_dolar = 20.54
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print("Dólar estadounidense: $" + dolar)
elif opcion == 2:
    pesos = input("Peso colombiano: ")
    pesos = float(pesos)
    valor_dolar = 3559.40
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print("Dólar estadounidense: $" + dolar)
elif opcion == 3:
    pesos = input("Peso argentino: ")
    pesos = float(pesos)
    valor_dolar = 91.57
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print("Dólar estadounidense: $" + dolar)
else:
    print('Opción invalida')