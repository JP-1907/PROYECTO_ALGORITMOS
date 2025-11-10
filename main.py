import funciones as f


menu = {
    "Salchichas": [
        {"nombre": "Salchicha normal", "precio": 5.00, "cantidad": 10, "es_vegano": False},
        {"nombre": "Salchicha vegana", "precio": 4.50, "cantidad": 12, "es_vegano": True},
        {"nombre": "Salchicha alemana", "precio": 6.00, "cantidad": 12, "es_vegano": False}
    ],
    "Pan": [
        {"nombre": "Normal", "precio": 2.00, "cantidad": 15, "tamaño": "mediano", "es_integral": False},
        {"nombre": "Grande", "precio": 3.00, "cantidad": 12, "tamaño": "grande", "es_integral": False},
        {"nombre": "Integral", "precio": 4.00, "cantidad": 10, "tamaño": "mediano", "es_integral": True}
    ],
    "Refrescos": [
        {"nombre": "Pepsi", "precio": 3.00, "cantidad": 20, "sabor": "Cola", "contiene_azucar": True},
        {"nombre": "Pepsi zero", "precio": 3.50, "cantidad": 18, "sabor": "Cola", "contiene_azucar": False},
        {"nombre": "Frescolita", "precio": 3.20, "cantidad": 15, "sabor": "naranja", "contiene_azucar": True}
    ]
}


def main():

    print("***********************************************************************")
    print("Te damos la bienvenida al sistema de gestión de Hot Dog CCS")
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

