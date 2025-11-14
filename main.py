import funciones as f
import json
import M_Inventario

try:
    with open("ingredientes.json", "r", encoding="utf-8") as file:
        menu_json = json.load(file)
except FileNotFoundError:
    print("Error: No se encontró el archivo ingredientes.json.")
    menu_json = []


productos = f.transformar_menu(menu_json)
inventario = M_Inventario.Inventario(productos)
clientes = []

print("***********************************************************************")
print("Te damos la bienvenida al sistema de gestión de Hot Dog CCS")
print("***********************************************************************\n")

while True:
    print("\n====Menú Principal====")
    print("1. Registrar cliente")
    print("2. Mostrar menú")
    print("3. Realizar compra")
    print("4. Gestión de Inventario") 
    print("5. Salir")
    print("6. Simular un día de ventas")
    print("7. Ver estadísticas")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        f.registrar_cliente(clientes)
    elif opcion == "2":
        f.mostrar_menu_hotdogs()
    elif opcion == "3":
        f.realizar_compra(clientes, productos) if productos else print("No se puede realizar la compra: menú vacío.")
    elif opcion == "4":
        f.menu_inventario(inventario)  
    elif opcion == "5": 
        print("Saliendo del sistema...")
        break
    elif opcion == "6":
        f.simular_ventas(productos, inventario)
    elif opcion == "7":
        f.mostrar_estadisticas()
    else:
        print("Opción no válida. Intente nuevamente.")









