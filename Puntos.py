puntos = float(input("Ingrese su puntuación:"))


if puntos <0.0 or puntos > 1.0:
    print("Fuera de Rango")
else:
    if puntos > 0.9:
        print("Sobresaliente")
    elif puntos >= 0.8 and puntos < 0.9:
        print("Notable")
    elif puntos >= 0.7 and puntos < 0.8:
        print("Bien")
    elif puntos >= 0.6 and puntos < 0.7:
        print("Satisfactorio")
    else:
        print("Insuficiente")