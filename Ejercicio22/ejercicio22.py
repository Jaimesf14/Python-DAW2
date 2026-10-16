#Datos de la partida
MARCAS_MODELOS = { "SEAT": ["Ibiza", "Leon", "Ateca", "Arona"], "Toyota": ["Corolla", "Yaris", "RAV4", "C-HR"] }
ventas = [
["SEAT", "Ibiza", 2024, 2023, 18000], ["SEAT", "Ibiza", 2024, 2024, 18500], ["SEAT", "Ibiza", 2024, 2024, 19000],
["SEAT", "Ibiza", 2025, 2024, 19500], ["SEAT", "Ibiza", 2025, 2025, 20000], ["SEAT", "Ibiza", 2025, 2025, 20200],
["SEAT", "Ibiza", 2026, 2025, 20500], ["SEAT", "Ibiza", 2026, 2026, 21000], ["SEAT", "Ibiza", 2026, 2026, 21500],
["SEAT", "Leon", 2024, 2024, 24000], ["SEAT", "Leon", 2024, 2024, 24500], ["SEAT", "Leon", 2024, 2023, 23800],
["SEAT", "Leon", 2025, 2025, 25500], ["SEAT", "Leon", 2025, 2025, 26000], ["SEAT", "Leon", 2025, 2024, 25200],
["SEAT", "Leon", 2026, 2026, 27000], ["SEAT", "Leon", 2026, 2026, 27500], ["SEAT", "Leon", 2026, 2025, 26800],
["SEAT", "Ateca", 2024, 2024, 28000], ["SEAT", "Ateca", 2025, 2025, 29500], ["SEAT", "Ateca", 2026, 2026, 31000],
["SEAT", "Arona", 2024, 2024, 21000], ["SEAT", "Arona", 2025, 2025, 22000], ["SEAT", "Arona", 2026, 2026, 23000],
["Toyota", "Corolla", 2024, 2024, 26000], ["Toyota", "Corolla", 2024, 2024, 26500], ["Toyota", "Corolla", 2024, 2023, 25800],
["Toyota", "Corolla", 2025, 2025, 27500], ["Toyota", "Corolla", 2025, 2025, 28000], ["Toyota", "Corolla", 2025, 2024, 27200],
["Toyota", "Corolla", 2026, 2026, 29000], ["Toyota", "Corolla", 2026, 2026, 29500], ["Toyota", "Corolla", 2026, 2025, 28800],
["Toyota", "Yaris", 2024, 2024, 20000], ["Toyota", "Yaris", 2025, 2025, 21000], ["Toyota", "Yaris", 2026, 2026, 22000],
["Toyota", "RAV4", 2024, 2024, 38000], ["Toyota", "RAV4", 2025, 2025, 39500], ["Toyota", "RAV4", 2026, 2026, 41000],
["Toyota", "C-HR", 2024, 2024, 31000], ["Toyota", "C-HR", 2025, 2025, 32500], ["Toyota", "C-HR", 2026, 2026, 34000]
]


opcion = 0
while opcion!=5:
    print("=== SISTEMA DE GESTIÓN DE VENTAS ===")
    print("| 1. Dar de alta una nueva venta")
    print("| 2. Resumen de ventas (Marca_Modelo_Año)")
    print("| 3. Resumen de ventas (Marca_Modelo - Todos los años)")
    print("| 4. Resumen de ventas (Marca - Todos los modelos y años)")
    print("| 5. Salir del programa")


    opcion = int(input("- Introduzca la opción que quieres elegir: "))

    match opcion:
        case 1:
            print("---------------------------------------------------------")
            print(f"--- MARCAS DISPONIBLES ---")
            for marca in MARCAS_MODELOS:
                print(f"| {marca}")
            marca_elegida = input("- Introduce la marca que quieres seleccionar: ")
            if marca_elegida in MARCAS_MODELOS:
                print(f"| Marca elegida = {marca_elegida}")
            else:
                print(f"Marca no valida.")  

            print(f"--- MODELOS DISPONIBLES ---")
            for modelo in MARCAS_MODELOS[marca_elegida]:
                print(f"| {modelo}")
            modelo_elegida = input("- Introduce el modelo que quieres seleccionar: ")
            if modelo_elegida in MARCAS_MODELOS[marca_elegida]:
                print(f"| Modelo elegido = {modelo_elegida}")
            else:
                print(f"Modelo no valido.")

           # while True:
            #    try:
             #       anio_venta = int(input(f"Introduce un año de venta entre 2024 y 2026"))  


            break;
        case 2:
            print("a")
            break
        case 3:
            print("a")
            break
        case 4:
            print("a")
            break
        case 5:
            print("Saliendo del menú...")
            break
        case _:
            print("a")
            break
