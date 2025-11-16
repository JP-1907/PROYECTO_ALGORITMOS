import funciones as f
import M_Inventario

# --- Inicialización ---
menu_json = f.cargar_datos_remotos()      
productos = f.transformar_menu(menu_json)    
inventario = M_Inventario.Inventario(productos)
clientes = []

print("Te damos la bienvenida al sistema de gestión de Hot Dog CCS")


while True:
    print("\n====Menú Principal====")
    print("1. Registrar cliente")
    print("2. Mostrar menú de hot dogs (inventario remoto)")
    print("3. Realizar compra de ingredientes")
    print("4. Gestión de Inventario") 
    print("5. Gestión del Menú de Hot Dogs") 
    print("6. Simular un día de ventas")
    print("7. Ver estadísticas")
    print("8. Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        f.registrar_cliente(clientes)

    elif opcion == "2":
        # Mostrar categorías y opciones desde el inventario remoto
        for categoria in menu_json:
            print(f"\n--- {categoria['Categoria'].upper()} ---")
            for opcion in categoria.get("Opciones", []):
                detalles = ", ".join(f"{k}: {v}" for k, v in opcion.items())
                print(f"   - {detalles}")

    elif opcion == "3":
        f.realizar_compra(clientes, productos) if productos else print("No se puede realizar la compra: inventario vacío.")

    elif opcion == "4":
        f.menu_inventario(inventario)

    elif opcion == "5":
        f.menu_gestion_hotdogs(inventario)

    elif opcion == "6":
        f.simular_ventas(productos, inventario)

    elif opcion == "7":
        f.mostrar_estadisticas()

    elif opcion == "8":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")

