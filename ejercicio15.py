#Enunciado: Añadir al ejercicio anterior una opción para salir del programa y un bucle del
#que sólo saldrá el programa cuando el usuario seleccione dicha opción de salida.
import ejercicio9
import ejercicio10
import ejercicio11
import ejercicio12
import ejercicio13

opcion = 0
while opcion!=6:
    print("=== EJERCICIOS DEL 9 AL 13 ===")
    print("| 1. Ejercicio 9")
    print("| 2. Ejercicio 10")
    print("| 3. Ejercicio 11")
    print("| 4. Ejercicio 12")
    print("| 5. Ejercicio 13")
    print("| 6. Salir")


    opcion = int(input("- Introduzca la opción que quieres elegir: "))

    match opcion:
        case 1:
            ejercicio9.ejecutar()
        case 2:
            ejercicio10.ejecutar()
        case 3:
            ejercicio11.ejecutar()
        case 4:
            ejercicio12.ejecutar()
        case 5:
            ejercicio13.ejecutar()
        case 6:
            print("Saliendo")
        case _:
            print("Opción no valida")