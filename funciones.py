from cliente import Cliente
from factura import Factura
import json
from producto import Pan, PerroProducto, Topping, Salsa, Acompañamiento
import json

def mostrar_menu_hotdogs():
    try:
        with open("menu.json", "r", encoding="utf-8") as file:
            menu = json.load(file)
    except FileNotFoundError:
        print("No se encontró el archivo menu.json.")
        return

    print("\n=== Menú de Hot Dogs ===")
    for i, item in enumerate(menu, start=1):
        nombre = item.get("nombre", "Sin nombre")
        pan = item.get("Pan", "N/A")
        salchicha = item.get("Salchicha", "N/A")
        toppings = ", ".join(item.get("toppings", [])) or "Sin toppings"
        salsas = ", ".join(item.get("salsas", item.get("Salsas", []))) or "Sin salsas"
        acompañante = item.get("Acompañante", "Sin acompañante")

        print(f"\n{i}. {nombre.upper()}")
        print(f"    Pan: {pan}")
        print(f"    Salchicha: {salchicha}")
        print(f"    Toppings: {toppings}")
        print(f"    Salsas: {salsas}")
        print(f"    Acompañante: {acompañante}")
def transformar_menu(menu_json):
    productos = []
    id_actual = 1

    for categoria_data in menu_json:
        categoria = categoria_data.get("Categoria", "").lower()
        opciones = categoria_data.get("Opciones", [])

        for item in opciones:
            nombre = item.get("nombre", "Sin nombre")
            precio = item.get("precio", 3.0)
            cantidad = item.get("cantidad", 40)

            if categoria == "pan":
                producto = Pan(
                    id=id_actual,
                    nombre=nombre,
                    precio=precio,
                    cantidad=cantidad,
                    tamaño=item.get("tamaño", 6)
                )

            elif categoria == "salchicha":
                producto = PerroProducto(
                    id=id_actual,
                    nombre=nombre,
                    precio=precio,
                    cantidad=cantidad,
                    tipo_salchicha=item.get("tipo", "vienesa")
                )

            elif categoria in ["topping", "toppings"]:
                producto = Topping(
                    id=id_actual,
                    nombre=nombre,
                    precio=precio,
                    cantidad=cantidad,
                    es_picante=item.get("es_picante", False)
                )

            elif categoria in ["salsa", "salsas"]:
                producto = Salsa(
                    id=id_actual,
                    nombre=nombre,
                    precio=precio,
                    cantidad=cantidad,
                    tipo=item.get("tipo", "cremosa")
                )

            elif categoria in ["acompañante", "acompañantes"]:
                if "no vendemos alcohol" in nombre.lower():
                    continue  # Ignorar productos con esa frase

                producto = Acompañamiento(
                    id=id_actual,
                    nombre=nombre,
                    precio=precio,
                    cantidad=cantidad,
                    tipo=item.get("tipo", "acompañante"),
                    detalles=item.get("detalles", [])
                )

            else:
                continue  # Ignorar categorías no reconocidas

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
from M_Inventario import Inventario, Pan, Acompañamiento, PerroProducto, Salsa, Topping

def menu_inventario(inventario: Inventario):
    while True:
        print("\n==== Gestión de Inventario ====")
        print("1. Visualizar inventario")
        print("2. Buscar por nombre")
        print("3. Listar por categoría")
        print("4. Actualizar existencia")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.visualizar_inventario()

        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            inventario.buscar_existencia_por_nombre(nombre)

        elif opcion == "3":
            print("Categorías disponibles: pan, salchicha, topping, salsa, acompañante")
            categoria = input("Ingrese la categoría: ").lower()

            if categoria == "pan":
                inventario.listar_por_categoria(Pan)
            elif categoria == "salchicha":
                inventario.listar_por_categoria(PerroProducto)
            elif categoria == "topping":
                inventario.listar_por_categoria(Topping)
            elif categoria == "salsa":
                inventario.listar_por_categoria(Salsa)
            elif categoria == "acompañante":
                inventario.listar_por_categoria(Acompañamiento)
            else:
                print("Categoría no reconocida.")

        elif opcion == "4":
            try:
                id_producto = int(input("ID del producto: "))
                nueva_cantidad = int(input("Nueva cantidad: "))
                inventario.actualizar_existencia(id_producto, nueva_cantidad)
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "5":
            break
        else:
            print("Opción no válida.")
def guardar_clientes(clientes, archivo="clientes.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump([vars(c) for c in clientes], f, ensure_ascii=False, indent=4)

def cargar_clientes(archivo="clientes.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return [Cliente(**data) for data in json.load(f)]
    except FileNotFoundError:
        return 
    
import random
def mostrar_estadisticas():
    print("Módulo de estadísticas aún no implementado. Simula al menos dos días para activarlo.")
def simular_ventas(productos, inventario):
    total_clientes = random.randint(0, 200)
    cambio_opinion = 0
    sin_compra = 0
    ventas = {}

    for i in range(total_clientes):
        cantidad_hotdogs = random.randint(0, 5)
        if cantidad_hotdogs == 0:
            print(f"El cliente {i} cambió de opinión")
            cambio_opinion += 1
            continue

        orden = []
        for _ in range(cantidad_hotdogs):
            hotdog = random.choice(productos)
            if hotdog.cantidad > 0:
                orden.append(hotdog)
            else:
                print(f"Cliente {i} no pudo comprar {hotdog.nombre} por falta de inventario")
                sin_compra += 1
                break

        if orden:
            for h in orden:
                h.cantidad -= 1
                ventas[h.nombre] = ventas.get(h.nombre, 0) + 1
            print(f"Cliente {i} compró {[h.nombre for h in orden]}")

    print("\n=== Resumen del día ===")
    print(f"Total clientes: {total_clientes}")
    print(f"Clientes sin compra: {sin_compra}")
    print(f"Clientes que cambiaron de opinión: {cambio_opinion}")
    print(f"Hot dogs vendidos: {ventas}")
