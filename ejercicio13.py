#Enunciado: Escribe un programa que pida al usuario su nombre y su apellido, y luego
#imprima un mensaje de bienvenida que combine ambos.
def ejecutar():
    nombre = input("Introduzca su nombre: ")
    apellido = input("Introduzca su apellido: ")
    print(f"Bienvenido {nombre} {apellido}!")