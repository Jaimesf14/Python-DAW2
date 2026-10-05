#Enunciado: Crea un programa que calcule el IMC (Índice de Masa Corporal) del usuario.
#El programa deberá pedir al usuario su peso (en kilogramos) y su altura (en metros), y
#luego calcular su IMC usando la fórmula: IMC = Peso / Altura^2

peso = float(input("Introduzca su peso en Kiligramos: "))
altura = float(input("Introduzca su altura en metros: "))

imc = float(peso / (altura*altura))

print(f"El IMC del usuario es {imc:.2f}")