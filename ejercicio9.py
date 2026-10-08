#Enunciado: Crea un programa que convierta metros a centímetros. El programa deberá
#pedir al usuario que introduzca una cantidad en metros y devolver la cantidad en
#centímetros.
def ejecutar():
    metros = float(input("Introduzca la cantidad de metros que desea pasar a centímetros: "))
    centimetros = metros * 100

    print(f"{metros} metros son {centimetros} centímetros")