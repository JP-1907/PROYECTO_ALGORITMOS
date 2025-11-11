from producto import Pan, Refresco, PerroProducto
from cliente import Cliente
from factura import Factura

def transformar_menu(menu_json):
    productos = []
    id_actual = 1

    for categoria_data in menu_json:
        categoria = categoria_data.get("Categoria", "")
        opciones = categoria_data.get("Opciones", [])

        for item in opciones:
            nombre = item.get("nombre", "Sin nombre")
            precio = 3.0  # Valor por defecto
            cantidad = 10  # Valor por defecto

            if categoria == "Pan":
                producto = Pan(
                    id=id_actual,
                    nombre=nombre,
                    precio=precio,
                    cantidad=cantidad,
                    tamaño=item.get("tamaño", 6),
                    es_integral=item.get("tipo", "").lower() == "trigo entero"
                )

            elif categoria == "Salchicha":
                producto = PerroProducto(
                    id=id_actual,
                    nombre=nombre,
                    precio=precio,
                    cantidad=cantidad,
                    es_vegano=item.get("tipo", "").lower() == "vegetal"
                )

            elif categoria == "Acompañante" and item.get("tipo", "").lower() == "refresco":
                producto = Refresco(
                    id=id_actual,
                    nombre=nombre,
                    precio=precio,
                    cantidad=cantidad,
                    sabor=nombre,
                    contiene_azucar="zero" not in nombre.lower()
                )

            else:
                continue  # Ignorar salsas, toppings, jugos, papas, etc.

            productos.append(producto)
            id_actual += 1

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
        print(f"{producto.id}. {producto}")

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
                try:
                    id_producto = int(input("Ingrese el ID del producto a agregar (o 0 para finalizar): "))
                except ValueError:
                    print("ID inválido. Intente nuevamente.")
                    continue

                if id_producto == 0:
                    break

                producto = buscar_producto_por_id(id_producto, productos)

                if producto:
                    try:
                        cantidad = int(input(f"Ingrese la cantidad de {producto.nombre}: "))
                    except ValueError:
                        print("Cantidad inválida.")
                        continue

                    if cantidad <= 0:
                        print("La cantidad debe ser mayor que cero.")
                    elif producto.cantidad >= cantidad:
                        productos_seleccionados.append((producto, cantidad))
                    else:
                        print("No hay suficiente cantidad del producto seleccionado.")
                else:
                    print(f"Producto con ID {id_producto} no encontrado.")

            if productos_seleccionados:
                factura = Factura(cliente, productos_seleccionados)
                factura.mostrar_factura()

                confirmar_pago = input("¿Desea confirmar la compra? (S/N): ")

                if confirmar_pago.upper() == "S":
                    for producto, cantidad in productos_seleccionados:
                        producto.cantidad -= cantidad
                    print("Compra realizada con éxito!")
                else:
                    print("Compra cancelada. No se modificó el inventario.")
            else:
                print("No se seleccionaron productos.")
            break
        else:
            print(f"Cliente con cédula {cedula} no registrado. ¿Desea registrarlo? (S/N): ")
            registrar_nuevo_cliente = input().upper()

            if registrar_nuevo_cliente == "S":
                registrar_cliente(clientes)
            else:
                print("\nRegresando al menú principal...\n")
