from producto import Cafe, Jugo, Postre
from cliente import Cliente
from factura import Factura

def transformar_menu(menu):
    productos = []

    for categoria in menu:
        for producto_data in menu[categoria]:
            if categoria == "postres":
                producto = Postre(
                    nombre=producto_data["nombre"],
                    precio=producto_data["precio"],
                    cantidad=producto_data["cantidad"],
                    es_vegano=producto_data["es_vegano"],
                    id= len(productos) + 1
                )
            elif categoria == "cafes":
                producto = Cafe(
                    nombre=producto_data["nombre"],
                    precio=producto_data["precio"],
                    cantidad=producto_data["cantidad"],
                    tamaño=producto_data["tamaño"],
                    es_descafeinado=producto_data["es_descafeinado"],
                    id= len(productos) + 1
                )
            else:
                producto = Jugo(
                    nombre=producto_data["nombre"],
                    precio=producto_data["precio"],
                    cantidad=producto_data["cantidad"],
                    sabor=producto_data["sabor"],
                    contiene_azucar=producto_data["contiene_azucar"],
                    id= len(productos) + 1
                )
            
            #Por qué no funciona poner el id aquí? producto.id = x. ¿Cómo hacemos que se pueda?
            productos.append(producto)

    return productos

def registrar_cliente(clientes):
    nombre = input("Ingrese el nombre del cliente: ")
    cedula = input("Ingrese la cédula del cliente: ")
    edad = int(input("Ingrese la edad del cliente: "))

    cliente = Cliente(nombre, cedula, edad)
    clientes.append(cliente)
    print(f"Cliente registrado con éxito: {cliente}\n")

def mostrar_menu(productos):
    for producto in productos:
        print(f"{producto.id}. {producto.__str__()}")

def buscar_cliente_por_cedula(cedula, clientes):
    for cliente in clientes:
        if cliente.cedula == cedula:
            return cliente
    return None

def buscar_producto_por_id(id_producto, productos):
    for producto in productos:
        if producto.id == id_producto:
            return producto
    return None

def realizar_compra(clientes, productos):
 
    while True:
        cedula = input("Ingrese la cédula del cliente: ")
        cliente = buscar_cliente_por_cedula(cedula, clientes)

        if cliente:
            mostrar_menu(productos)

            productos_seleccionados = []
            while True:
                id_producto = int(input("Ingrese el ID del producto a agregar (o 0 para finalizar): "))

                if id_producto == 0:
                    break
                
                producto = buscar_producto_por_id(id_producto, productos)

                if producto:
                    cantidad = int(input(f"Ingrese la cantidad de {producto.nombre}: "))

                    if producto.cantidad >= cantidad: #Esta es una de las validaciones. Deberían validar tambien que el cliente no ponga nro negativo o 0
                        productos_seleccionados.append((producto, cantidad)) #Tuplas
                    else:
                        print("No hay suficiente cantidad del producto seleccionado.")
                else:
                    print(f"Producto con ID {id_producto} no encontrado.")


            # Crear factura
            factura = Factura(cliente, productos_seleccionados)

            # Mostrar factura
            factura.mostrar_factura()

            confirmar_pago = input("¿Desea confirmar la compra? (S/N): ")

            if confirmar_pago.upper() == "S":
                for producto, cantidad in productos_seleccionados:
                    producto.cantidad -= cantidad  # Resta la cantidad solo si se confirma la compra

                print("Compra realizada con éxito!")
                break
            else:
                print("Compra cancelada.") #Aún así se resta del inventario. Corregir
        else:
            print(f"Cliente con cédula {cedula} no registrado. ¿Desea registrarlo? (S/N): ")
            registrar_nuevo_cliente = input().upper()

            if registrar_nuevo_cliente == "S":
                registrar_cliente(clientes)
            else:
                print("\nRegresando al menú principal...\n")
                break