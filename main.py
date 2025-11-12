def main():
    print("***********************************************************************")
    print("Te damos la bienvenida al sistema de gestión de Hot Dog CCS")
    print("***********************************************************************\n")

    while True:
        print("\n====Menú Principal====")
        print("1. Registrar cliente")
        print("2. Mostrar menú (Productos disponibles para la venta)")
        print("3. Realizar compra")
        print("4. Gestión de Inventario") # Nueva Opción
        print("5. Salir") # Opción Salir ahora es 5

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            f.registrar_cliente(clientes)
        elif opcion == "2":
            if productos:
                f.mostrar_menu(productos)
            else:
                print("No hay productos disponibles.")
        elif opcion == "3":
            if productos:
                # La función realizar_compra ya actualiza la cantidad en el objeto producto,
                # lo cual se refleja automáticamente en el Inventario.
                f.realizar_compra(clientes, productos) 
            else:
                print("No se puede realizar la compra: menú vacío.")
        elif opcion == "4":
            # Manejar el submenú de inventario
            menu_inventario(inventario)
        elif opcion == "5": # Nueva opción de salir
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


