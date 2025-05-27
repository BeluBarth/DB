# Integrantes del grupo:
# María Laura Rosano DNI 31116820
# Federico Barth DNI 32739193
# María Belén Barth DNI 36139331
# Veronica Analia Gagliardi DNI 32605956 

# Proposito del sistema es implementar un Gestor digital básico que le permita gestionar la venta de pasajes
# Inicia el programa 
print("Bienvenidos a SkyRoute - Sistema de Gestion de Pasajes")

opcion = ""  # Inicializamos la variable

# Bucle que se repite hasta que el usuario elija "8"
while opcion != "8":
    print("\nMenu Principal")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Consultar Ventas")
    print("5. Boton de Arrepentimiento")
    print("6. Ver Reporte General")
    print("7. Acerca del sistema")
    print("8. Salir")

    opcion = input("Seleccionar una opción: ")

    if opcion == "1":
        print("\n-- GESTIONAR CLIENTES --")
        print("1. Ver Clientes")
        print("2. Agregar Clientes")
        print("3. Modificar Cliente")
        print("4. Eliminar Clientes")
        print("5. Volver al Menu Principal")
        subopcion = input("Selecciona una opción del submenú: ")

        if subopcion == "1": 
            print("Mostrando Clientes...")
        elif subopcion == "2":
            nombre = input("Nombre del cliente: ")
            email = input("Email: ")
            print(f"Cliente guardado: {nombre} - {email}")
        elif subopcion == "3": 
            print("Modificando Cliente...")
        elif subopcion == "4":
            print("Eliminando Cliente...")
        elif subopcion == "5":
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida.")

    elif opcion == "2":
        print("\n-- GESTIONAR DESTINOS --")
        print("1. Ver Destinos")
        print("2. Agregar Destino")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        print("5. Volver al Menu Principal")
        subopcion = input("Selecciona una opción del submenú: ")

        if subopcion == "1":
            print("Mostrando Destinos...")
        elif subopcion == "2":
            ciudad = input("Ciudad: ")
            pais = input("País: ")
            precio = input("Precio: ")
            print(f"Destino guardado: {ciudad}, {pais} - ${precio}")
        elif subopcion == "3":
            print("Modificando destino...")
        elif subopcion == "4":
            print("Eliminando destino...")
        elif subopcion == "5":
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida.")

    elif opcion == "3":
        print("\n-- GESTIONAR VENTAS --")
        cliente = input("Cliente: ")
        destino = input("Destino: ")
        print(f"Venta registrada: {cliente} -> {destino}")

    elif opcion == "4":
        print("\n-- CONSULTAR VENTAS --")
        print("1. Ver todas las ventas")
        print("2. Ver por cliente")
        print("3. Ver de la última semana")
        print("4. Volver al menú principal")
        subopcion = input("Selecciona una opción del submenú: ")

        if subopcion == "1":
            print("Todas las ventas...")
        elif subopcion == "2":
            print("Ventas por cliente...")
        elif subopcion == "3":
            print("Ventas de la última semana...")
        elif subopcion == "4":
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida.")

    elif opcion == "5":
        print("\n-- BOTÓN DE ARREPENTIMIENTO --")
        print("Anulando última venta...")

    elif opcion == "6":
        print("\n-- REPORTE GENERAL --")
        print("Mostrando resumen del sistema...")

    elif opcion == "7":
        print("\n-- ACERCA DEL SISTEMA --")
        print("SkyRoute - Sistema de Gestión de Pasajes")
        print("Versión: Prototipo 1.0")

    elif opcion == "8":
        print("Gracias por usar SkyRoute. ¡Hasta pronto!")

    else:
        print("Opción inválida. Intente nuevamente.")