#parte 2
contador = 0
suma = 0
while True:
        numero = input ("Introduzca un número:")
        if (numero =="fin"):
         break 
        contador = contador + 1
        suma = suma + int(numero)
print("Contador", contador)
print("Suma", suma)
print("Promedio", suma/contador)