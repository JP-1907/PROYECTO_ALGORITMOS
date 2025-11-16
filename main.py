import funciones as f
from M_Inventario import Inventario

def main():
    print("=== Bienvenido al Sistema de Gestión de Hot Dogs ===")

    # 1. Cargar inventario desde ingredientes.json
    ingredientes_json = f.cargar_inventario_remoto()
    productos = f.transformar_inventario(ingredientes_json)
    inventario = Inventario(productos)

    # 2. Cargar lista de hot dogs (recetas completas)
    hotdogs_json = f.cargar_menu()

    # 3. Menú principal
    while True:
        print("\n==== Menú Principal ====")
        print("1. Gestión de clientes")
        print("2. Gestión de inventario")
        print("3. Gestión de hot dogs")
        print("4. Simular ventas")
        print("5. Mostrar estadisticas")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clientes = f.cargar_clientes()
            f.realizar_compra(clientes, productos)
            f.guardar_clientes(clientes)

        elif opcion == "2":
            f.menu_inventario(inventario)

        elif opcion == "3":
            f.menu_gestion_hotdogs(inventario, hotdogs_json)

        elif opcion == "4":
            resultado = f.simular_ventas(productos, inventario)
            print("\n=== Resumen del día ===")
            print(f"Total clientes: {resultado['total_clientes']}")
            print(f"Clientes sin compra: {resultado['sin_compra']}")
            print(f"Clientes que cambiaron de opinión: {resultado['cambio_opinion']}")
            print(f"Productos vendidos: {resultado['ventas']}")
        elif opcion == "5":
            f.mostrar_estadisticas()
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
        main()
