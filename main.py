import funciones as f
import json

# Cargar el menú desde ingredientes.json
try:
    with open("ingredientes.json", "r", encoding="utf-8") as file:
        menu_json = json.load(file)
except FileNotFoundError:
    print("Error: No se encontró el archivo ingredientes.json.")
    menu_json = []

# Transformar el menú en objetos de producto
productos = f.transformar_menu(menu_json)
clientes = []

def main():
    print("***********************************************************************")
    print("Te damos la bienvenida al sistema de gestión de Hot Dog CCS")
    print("***********************************************************************\n")

    while True:
        print("\n====Menú principal====")
        print("1. Registrar cliente")
        print("2. Mostrar menú")
        print("3. Realizar compra")
        print("4. Salir")

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
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

main()

