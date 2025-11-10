import funciones as f


menu = {
    "postres": [
        {"nombre": "Torta de chocolate", "precio": 5.00, "cantidad": 10, "es_vegano": False},
        {"nombre": "Torta de frutas", "precio": 4.50, "cantidad": 12, "es_vegano": True},
        {"nombre": "Torta de helado", "precio": 6.00, "cantidad": 8, "es_vegano": False}
    ],
    "cafes": [
        {"nombre": "Espresso", "precio": 2.00, "cantidad": 15, "tamaño": "pequeño", "es_descafeinado": False},
        {"nombre": "Capuccino", "precio": 3.00, "cantidad": 12, "tamaño": "mediano", "es_descafeinado": False},
        {"nombre": "Moka", "precio": 4.00, "cantidad": 10, "tamaño": "grande", "es_descafeinado": False}
    ],
    "jugos": [
        {"nombre": "Jugo de naranja", "precio": 3.00, "cantidad": 20, "sabor": "naranja", "contiene_azucar": True},
        {"nombre": "Jugo de manzana", "precio": 2.50, "cantidad": 18, "sabor": "manzana", "contiene_azucar": False},
        {"nombre": "Jugo de plátano", "precio": 2.00, "cantidad": 15, "sabor": "cambur", "contiene_azucar": False}
    ]
}


def main():

    print("***********************************************************************")
    print("Te damos la bienvenida al sistema de gestión de la Cafetería CoffeeLove")
    print("***********************************************************************\n")

    while True:
        print("\n***Menú principal***")
        print("1. Registrar cliente")
        print("2. Mostrar menú")
        print("3. Realizar compra")
        print("4. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            f.registrar_cliente(clientes)
        elif opcion == "2":
            f.mostrar_menu(productos)
        elif opcion == "3":
            f.realizar_compra(clientes, productos)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Inicialización de datos (lista de productos y lista de clientes)
productos = f.transformar_menu(menu)
clientes = []

# Ejecución del menú principal
main()