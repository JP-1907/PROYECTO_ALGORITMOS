def main():
    print("***********************************************************************")
    print("Te damos la bienvenida al sistema de gestión de Hot Dog CCS")
    print("***********************************************************************\n")

    while True:
        print("\n====Menú Principal====")
        print("1. Registrar cliente")
        print("2. Mostrar menú (Productos disponibles para la venta)")
        print("3. Realizar compra")
        print("4. Gestión de Inventario") 
        print("5. Salir") 

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
                f.realizar_compra(clientes, productos) 
            else:
                print("No se puede realizar la compra: menú vacío.")
        elif opcion == "4":
            menu_inventario(inventario)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


