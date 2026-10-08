#Enunciado: Meter en un match / case los ejercicios del 9 al 13, de forma que aparezca un
#menú con las 5 opciones para que el usuario decida que ejercicio o enunciado quiere
#ejecutar.
import ejercicio9
import ejercicio10
import ejercicio11
import ejercicio12
import ejercicio13

print("=== EJERCICIOS DEL 9 AL 13 ===")
print("| 1. Ejercicio 9")
print("| 2. Ejercicio 10")
print("| 3. Ejercicio 11")
print("| 4. Ejercicio 12")
print("| 5. Ejercicio 13")

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
    case _:
        print("Opción no valida")
