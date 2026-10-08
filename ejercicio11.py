#Enunciado: Escribe un programa que calcule el importe total a pagar en un restaurante. El
#programa deberá pedir al usuario el coste de la comida y el porcentaje de propina que
#quiere dejar, y luego devolver el importe total

def ejecutar():
    costeComida = float(input("Introduzca el  coste  de la comida: "))
    porcentajePropina = int(input("Introduzca el porcentaje de propina que desea dejar: "))

    resultado = float(costeComida + ((porcentajePropina/100)*costeComida))

    print(f"El importe total de {costeComida} con un porcentaje  de propinas del {porcentajePropina}% es: {resultado:.2f}")