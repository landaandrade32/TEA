def calcularSalario(horas,tarifa): 
    horas_extras = horas - MAX_HORAS_SEMANALES
    if (horas_extras > 0):
        salario = (MAX_HORAS_SEMANALES * tarifa) + (horas_extras * (tarifa * 1.5))
    else: 
        salario= horas * tarifa 
    return salario

try:
    MAX_HORAS_SEMANALES = 40
    horas = int(input("ingrese numero de horas:"))
    tarifa = float(input("ingrese tarifa por hora:"))
    salario = calcularSalario(horas, tarifa)
    print(salario)
except:
    print("#Error, debe ingresar un valor numerico")