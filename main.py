import Manejo_Inventario
from producto import Pan, Refresco, PerroProducto
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
    # Crear productos iniciales
    productos = [
        Pan(1, "Pan de perro", 50),
        Refresco(2, "Coca-Cola", 30),
        PerroProducto(3, "Salchicha", 100)
    ]

    inventario = Inventario(productos)

    while True:
        print("\n==== Menú Principal ====")
        print("1. Ver inventario")
        print("2. Buscar producto por nombre")
        print("3. Buscar producto por ID")
        print("4. Listar por categoría")
        print("5. Actualizar stock")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.visualizar_inventario()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ")
            inventario.buscar_existencia_por_nombre(nombre)
        elif opcion == "3":
            id_producto = int(input("Ingrese el ID del producto: "))
            inventario.buscar_existencia_por_id(id_producto)
        elif opcion == "4":
            print("Categorías: Pan, Refresco, PerroProducto")
            categoria = input("Ingrese la categoría: ")
            if categoria == "Pan":
                inventario.listar_por_categoria(Pan)
            elif categoria == "Refresco":
                inventario.listar_por_categoria(Refresco)
            elif categoria == "PerroProducto":
                inventario.listar_por_categoria(PerroProducto)
            else:
                print("Categoría no válida.")
        elif opcion == "5":
            id_producto = int(input("Ingrese el ID del producto: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario.actualizar_existencia(id_producto, nueva_cantidad)
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()






