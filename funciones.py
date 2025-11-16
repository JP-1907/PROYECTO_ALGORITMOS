import matplotlib.pyplot as plt
import requests
from cliente import Cliente
from factura import Factura
import json
from producto import Pan, PerroProducto, Topping, Salsa, Acompañamiento, Producto
from M_Inventario import Inventario
import random
from typing import List, Optional  
import funciones as f
URL_DATOS = "https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-1/main/menu.json"
URL_INGREDIENTES = "https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-1/main/ingredientes.json"
estadisticas_dias = [] 

def cargar_inventario_remoto():
    """Carga inventario desde ingredientes.json en GitHub y limpia entradas no válidas."""
    try:
        response = requests.get(URL_INGREDIENTES, timeout=10)
        response.raise_for_status()
        data = response.json()  # lista de categorías y opciones

        for categoria in data:
            if categoria.get("Categoria", "").lower() == "acompañante":
                opciones_limpias = []
                for opcion in categoria.get("Opciones", []):
                    nombre = opcion.get("nombre", "").lower()
                    if "no vendemos alcohol" in nombre:
                        continue
                    opciones_limpias.append(opcion)
                categoria["Opciones"] = opciones_limpias

        return data
    except Exception as e:
        print(f"Error al cargar inventario desde el link: {e}")
        return []

def transformar_inventario(ingredientes_json):
    productos = []
    id_counter = 1

    for categoria in ingredientes_json:
        nombre_categoria = categoria.get("Categoria", "").lower()
        opciones = categoria.get("Opciones", [])

        if nombre_categoria == "pan":
            for opcion in opciones:
                productos.append(Pan(
                    id=id_counter,
                    nombre=opcion["nombre"],
                    precio=1.5,
                    cantidad=opcion.get("cantidad", 100),
                    tamaño=opcion.get("tamaño", 0)
                ))
                id_counter += 1

        elif nombre_categoria == "salchicha":
            for opcion in opciones:
                productos.append(PerroProducto(
                    id=id_counter,
                    nombre=opcion["nombre"],
                    precio=2.0,
                    cantidad=opcion.get("cantidad", 100),
                    tipo_salchicha=opcion.get("tipo", "vienesa")
                ))
                id_counter += 1

        elif nombre_categoria == "acompañante":
            for opcion in opciones:
                if opcion== "No vendemos alcohol":
                    continue
                productos.append(Acompañamiento(
                    id=id_counter,
                    nombre=opcion["nombre"],
                    precio=1.0,
                    cantidad=opcion.get("cantidad", 100),
                    tipo=opcion.get("tipo", "bebida"),
                    detalles=[f"{opcion.get('tamaño', '')} {opcion.get('unidad', '')}"]
                ))
                id_counter += 1

        elif nombre_categoria == "salsa":
            for opcion in opciones:
                productos.append(Salsa(
                    id=id_counter,
                    nombre=opcion["nombre"],
                    precio=0.3,
                    cantidad=opcion.get("cantidad", 100),
                    tipo=opcion.get("base", "cremosa")
                ))
                id_counter += 1

        elif nombre_categoria == "topping":
            for opcion in opciones:
                productos.append(Topping(
                    id=id_counter,
                    nombre=opcion["nombre"],
                    precio=0.5,
                    cantidad=opcion.get("cantidad", 100),
                    es_picante=opcion.get("picante", False)
                ))
                id_counter += 1

    return productos
def cargar_datos_remotos():
    """Carga inventario desde el link remoto en GitHub (lista de categorías)."""
    try:
        resp = requests.get(URL_DATOS, timeout=10)
        resp.raise_for_status()
        data = resp.json()   
        return data          
    except Exception as e:
        print(f"Error al cargar datos desde el link: {e}")
        return []


def mostrar_menu_hotdogs(hotdogs_json):
    """Muestra el menú de hot dogs desde la lista remota."""
    if not hotdogs_json:
        print("El menú de hot dogs está vacío.")
        return

    print("\n=== Menú de Hot Dogs ===")
    for i, item in enumerate(hotdogs_json, start=1):
        nombre = item.get("nombre", "Sin nombre")
        pan = item.get("Pan", "N/A")
        salchicha = item.get("Salchicha", "N/A")
        toppings = ", ".join(item.get("toppings", [])) or "Sin toppings"
        salsas = ", ".join(item.get("salsas", [])) or "Sin salsas"
        acompañante = item.get("Acompañante", "Sin acompañante")

        print(f"\n{i}. {nombre.upper()}")
        print(f"    Pan: {pan}")
        print(f"    Salchicha: {salchicha}")
        print(f"    Toppings: {toppings}")
        print(f"    Salsas: {salsas}")
        print(f"    Acompañante: {acompañante}")

def transformar_menu(menu_json):
    productos = []
    id_counter = 1

    for categoria in menu_json:
        nombre_categoria = categoria.get("Categoria", "").lower()
        opciones = categoria.get("Opciones", [])

        if nombre_categoria == "pan":
            for opcion in opciones:
                productos.append(Pan(
                    id=id_counter,
                    nombre=opcion["nombre"],
                    precio=1.5,
                    cantidad=100,
                    tamaño=opcion.get("tamaño", 0)
                ))
                id_counter += 1

        elif nombre_categoria == "salchicha":
            for opcion in opciones:
                productos.append(PerroProducto(
                    id=id_counter,
                    nombre=opcion["nombre"],
                    precio=2.0,
                    cantidad=100,
                    tipo_salchicha=opcion.get("tipo", "vienesa")
                ))
                id_counter += 1

        elif nombre_categoria == "acompañante":
            for opcion in opciones:
                productos.append(Acompañamiento(
                    id=id_counter,
                    nombre=opcion["nombre"],
                    precio=1.0,
                    cantidad=100,
                    tipo=opcion.get("tipo", "bebida"),
                    detalles=[f"{opcion.get('tamaño', '')} {opcion.get('unidad', '')}"]
                ))
                id_counter += 1

        elif nombre_categoria == "salsa":
            for opcion in opciones:
                productos.append(Salsa(
                    id=id_counter,
                    nombre=opcion["nombre"],
                    precio=0.3,
                    cantidad=100,
                    tipo=opcion.get("base", "cremosa")
                ))
                id_counter += 1

        elif nombre_categoria == "toppings": 
            for opcion in opciones:
                productos.append(Topping(
                    id=id_counter,
                    nombre=opcion["nombre"],
                    precio=0.5,
                    cantidad=100,
                    es_picante=False
                ))
                id_counter += 1

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
        print(f"{producto.id}. {producto.nombre}: {producto.cantidad} en stock")

def buscar_cliente_por_cedula(cedula, clientes):
    for cliente in clientes:
        if cliente.cedula == cedula:
            return cliente
    return None

def buscar_producto_por_id(id_producto, productos: List[Producto]) -> Optional[Producto]:
    for producto in productos:
        if producto.id == id_producto:
            return producto
    return None

def realizar_compra(clientes, productos):
    while True:
        cedula = input("Ingrese la cédula del cliente: ")
        cliente = buscar_cliente_por_cedula(cedula, clientes)

        if cliente:
            print("\n--- Productos Disponibles ---")
            for p in productos:
                print(f"{p.id}. {p.nombre} (Stock: {p.cantidad})")

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
                        print(f"No hay suficiente cantidad del producto seleccionado ({producto.cantidad} en stock).")
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
        return []

def mostrar_estadisticas():
    if len(estadisticas_dias) < 2:
        print("⚠️ Debes simular al menos 2 días para ver estadísticas.")
        return

    dias = [d["dia"] for d in estadisticas_dias]
    clientes = [d["total_clientes"] for d in estadisticas_dias]
    sin_compra = [d["sin_compra"] for d in estadisticas_dias]
    cambio_opinion = [d["cambio_opinion"] for d in estadisticas_dias]

    plt.figure(figsize=(12,8))

    # Gráfico de clientes
    plt.subplot(2,1,1)
    plt.plot(dias, clientes, marker='o', label="Total clientes", color="blue")
    plt.plot(dias, sin_compra, marker='x', label="Sin compra", color="red")
    plt.plot(dias, cambio_opinion, marker='s', label="Cambio de opinión", color="orange")
    plt.title("Estadísticas de clientes por día")
    plt.xlabel("Día")
    plt.ylabel("Cantidad")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)

    # Gráfico de productos vendidos acumulados
    plt.subplot(2,1,2)
    ventas_totales = {}
    for d in estadisticas_dias:
        for prod, cant in d["ventas"].items():
            ventas_totales[prod] = ventas_totales.get(prod, 0) + cant

    productos = list(ventas_totales.keys())
    cantidades = list(ventas_totales.values())

    plt.bar(productos, cantidades, color="green")
    plt.title("Productos vendidos acumulados")
    plt.xlabel("Producto")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout(pad=3.0)
    plt.show()
def simular_ventas(productos, inventario, dia_numero=None):
    total_clientes = random.randint(0, 200)
    cambio_opinion = 0
    sin_compra = 0
    ventas = {}

    productos_disponibles = [p for p in productos if p.cantidad > 0]

    for i in range(total_clientes):
        cantidad_productos = random.randint(0, 5)
        if cantidad_productos == 0:
            cambio_opinion += 1
            continue

        orden = []
        for _ in range(cantidad_productos):
            if not productos_disponibles:
                sin_compra += 1
                break

            producto_elegido = random.choice(productos_disponibles)
            if producto_elegido.cantidad > 0:
                orden.append(producto_elegido)
            else:
                productos_disponibles.remove(producto_elegido)
                sin_compra += 1
                break
        
        if orden:
            for p in orden:
                p.cantidad -= 1 
                ventas[p.nombre] = ventas.get(p.nombre, 0) + 1

    # Guardar estadísticas del día
    estadisticas_dias.append({
        "dia": dia_numero if dia_numero else len(estadisticas_dias) + 1,
        "total_clientes": total_clientes,
        "sin_compra": sin_compra,
        "cambio_opinion": cambio_opinion,
        "ventas": ventas
    })

    # 👉 Retornar resultados como diccionario
    return {
        "total_clientes": total_clientes,
        "sin_compra": sin_compra,
        "cambio_opinion": cambio_opinion,
        "ventas": ventas
    }

def guardar_menu(menu):
    """Guarda el menú actual en menu.json."""
    try:
        with open("menu.json", "w", encoding="utf-8") as file:
            json.dump(menu, file, ensure_ascii=False, indent=4)
        print("Menú actualizado en menu.json.")
    except Exception as e:
        print(f"Error al guardar el menú: {e}")

def cargar_menu():
    """Carga el menú desde el link de GitHub."""
    try:
        response = requests.get(URL_DATOS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al cargar el menú desde el link: {e}")
        return []

def obtener_producto_por_nombre(nombre_producto: str, productos: List[Producto]) -> Optional[Producto]:
    """Busca un producto base por nombre en la lista de productos del inventario."""
    nombre_lower = nombre_producto.lower()
    for producto in productos:
        if producto.nombre.lower() == nombre_lower:
            return producto
    return None

def verificar_inventario_hotdog(hotdog: dict, inventario: Inventario) -> bool:
    """Verifica si hay suficiente inventario para un hot dog específico."""
    ingredientes = [hotdog.get("Pan"), hotdog.get("Salchicha")] + \
                   hotdog.get("toppings", []) + hotdog.get("salsas", [])
    

    acompañante = hotdog.get("Acompañante")
    if acompañante and "no vendemos alcohol" not in acompañante.lower():
        ingredientes.append(acompañante)

    print(f"\n--- Verificando Inventario para {hotdog['nombre'].upper()} ---")
    todo_disponible = True

    for ingrediente_nombre in set(ingredientes): 
        producto = obtener_producto_por_nombre(ingrediente_nombre, inventario.productos)
        
        if not producto:
            print(f"Ingrediente '{ingrediente_nombre}' NO ENCONTRADO en el inventario de ingredientes base.")
            todo_disponible = False
            continue
        cantidad_requerida = 1 
        if ingrediente_nombre in hotdog.get("toppings", []) or ingrediente_nombre in hotdog.get("salsas", []):
             cantidad_requerida = ingredientes.count(ingrediente_nombre)

        if producto.cantidad >= cantidad_requerida:
            print(f"Ingrediente '{ingrediente_nombre}': {producto.cantidad} en stock.")
        else:
            print(f"Ingrediente '{ingrediente_nombre}': Stock bajo ({producto.cantidad}). Se requieren {cantidad_requerida}.")
            todo_disponible = False

    if todo_disponible:
        print(f"\nInventario SUFICIENTE para el hot dog {hotdog['nombre'].upper()}.")
    else:
        print(f"\nInventario INSUFICIENTE/INCOMPLETO para el hot dog {hotdog['nombre'].upper()}.")

    return todo_disponible

def obtener_ingrediente(productos: List[Producto], categoria: type, mensaje: str, es_opcional: bool = False, validacion_size: Optional[int] = None) -> tuple[Optional[str], Optional[int]]: # <--- Se usa List y Optional
    """Función auxiliar para seleccionar un ingrediente con validación."""
    while True:
        print(f"\n--- Seleccionar {mensaje} ---")
        ingredientes_disponibles = []
        for p in productos:
            if isinstance(p, categoria):
                if categoria in (Pan, PerroProducto) and hasattr(p, 'tamaño'):
                    ingredientes_disponibles.append(p)
                    print(f"ID: {p.id}. {p.nombre} (Tamaño: {p.tamaño}, Stock: {p.cantidad})")
                else:
                    ingredientes_disponibles.append(p)
                    print(f"ID: {p.id}. {p.nombre} (Stock: {p.cantidad})")

        if es_opcional:
            print("0. Omitir/Ninguno")
        
        try:
            seleccion_id = input(f"Ingrese el ID del {mensaje}: ")
            if es_opcional and seleccion_id == '0':
                return None, None

            seleccion_id = int(seleccion_id)
            seleccionado = buscar_producto_por_id(seleccion_id, productos)

            if seleccionado and isinstance(seleccionado, categoria):
                if seleccionado.cantidad <= 0:
                    print(f"⚠️ Advertencia: El ingrediente '{seleccionado.nombre}' está AGOTADO. Por favor, seleccione otro o cancele.")
                    continue

                if validacion_size is not None and categoria in (Pan, PerroProducto):
                    if seleccionado.tamaño != validacion_size:
                        print(f"⚠️ ADVERTENCIA DE TAMAÑO: El '{seleccionado.nombre}' tiene un tamaño de {seleccionado.tamaño}, diferente al requerido ({validacion_size}).")
                        confirmar = input("¿Desea continuar con esta selección? (S/N): ").upper()
                        if confirmar != 'S':
                            continue
                
                return seleccionado.nombre, seleccionado.tamaño if hasattr(seleccionado, 'tamaño') else None
            else:
                print("ID no encontrado o no corresponde a la categoría.")

        except ValueError:
            print("ID inválido.")

def agregar_hotdog(inventario: Inventario):
    """Permite al usuario agregar un nuevo hot dog al menú con opción de salir en cualquier paso."""
    menu = cargar_datos_remotos()  
    productos = inventario.productos
    

    nombre_hotdog = input("Ingrese el nombre del nuevo Hot Dog (o 'salir' para cancelar): ").strip().lower()
    if nombre_hotdog == "salir":
        print("Proceso cancelado. Regresando al menú principal...")
        return
    if any(item.get("nombre", "").lower() == nombre_hotdog for item in menu):
        print("Ya existe un Hot Dog con ese nombre.")
        return
    
    print("\n--- AGREGAR NUEVO HOT DOG ---")

 
    pan_nombre, pan_tamaño = obtener_ingrediente(productos, Pan, "Pan")
    if pan_nombre is None or pan_nombre.lower() == "salir":
        print("Proceso cancelado.")
        return 
    

    salchicha_nombre, salchicha_tamaño = obtener_ingrediente(productos, PerroProducto, "Salchicha", validacion_size=pan_tamaño)
    if salchicha_nombre is None or salchicha_nombre.lower() == "salir":
        print("Proceso cancelado.")
        return

    toppings_nombres = []
    print("\n--- Seleccionar Toppings (Ingrese 'fin' para terminar o 'salir' para cancelar) ---")
    while True:
        topping_nombre, _ = obtener_ingrediente(productos, Topping, f"Topping #{len(toppings_nombres) + 1}", es_opcional=True)
        if topping_nombre is None:
            break
        if topping_nombre.lower() == "salir":
            print("Proceso cancelado.")
            return
        toppings_nombres.append(topping_nombre)
        
    salsas_nombres = []
    print("\n--- Seleccionar Salsas (Ingrese 'fin' para terminar o 'salir' para cancelar) ---")
    while True:
        salsa_nombre, _ = obtener_ingrediente(productos, Salsa, f"Salsa #{len(salsas_nombres) + 1}", es_opcional=True)
        if salsa_nombre is None:
            break
        if salsa_nombre.lower() == "salir":
            print("Proceso cancelado.")
            return
        salsas_nombres.append(salsa_nombre)


    acompañante_nombre, _ = obtener_ingrediente(productos, Acompañamiento, "Acompañante", es_opcional=True)
    if acompañante_nombre and acompañante_nombre.lower() == "salir":
        print("Proceso cancelado.")
        return
    if acompañante_nombre is None:
        acompañante_nombre = "Sin acompañante"


    nuevo_hotdog = {
        "nombre": nombre_hotdog,
        "Pan": pan_nombre,
        "Salchicha": salchicha_nombre,
        "toppings": toppings_nombres,
        "salsas": salsas_nombres,
        "Acompañante": acompañante_nombre if acompañante_nombre != "Sin acompañante" else None
    }


    print("\n--- Resumen del Nuevo Hot Dog ---")
    print(json.dumps(nuevo_hotdog, indent=4, ensure_ascii=False))

    verificar_inventario_hotdog(nuevo_hotdog, inventario)

    confirmar = input("¿Confirmar la adición del Hot Dog al menú? (S/N o 'salir' para cancelar): ").upper()
    if confirmar == 'S':
        menu.append(nuevo_hotdog)
        print(f"Hot Dog '{nombre_hotdog.upper()}' agregado al menú (solo en memoria).")
    else:
        print("Adición de Hot Dog cancelada.")

def eliminar_hotdog(inventario: Inventario):
    menu = cargar_menu()
    if not menu:
        print("El menú está vacío. No hay Hot Dogs para eliminar.")
        return

    print("\n=== Hot Dogs para Eliminar ===")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item.get('nombre').upper()}")

    try:
        opcion = int(input("Ingrese el número del Hot Dog a eliminar: "))
        if 1 <= opcion <= len(menu):
            hotdog_a_eliminar = menu[opcion - 1]
            nombre_hotdog = hotdog_a_eliminar.get("nombre", "Sin nombre").upper()
            hay_inventario_suficiente = verificar_inventario_hotdog(hotdog_a_eliminar, inventario)

            if hay_inventario_suficiente:
                print(f"\n⚠️ Advertencia: Aún hay inventario de los ingredientes para el Hot Dog '{nombre_hotdog}'.")
                confirmar = input("¿Realmente desea ELIMINAR este Hot Dog del menú? (S/N): ").upper()
                if confirmar == 'S':
                    menu.pop(opcion - 1)
                    guardar_menu(menu)
                    print(f"Hot Dog '{nombre_hotdog}' eliminado del menú.")
                else:
                    print(f"Eliminación de Hot Dog '{nombre_hotdog}' cancelada.")
            else:
                confirmar = input(f"El inventario es insuficiente para '{nombre_hotdog}'. ¿Confirmar la eliminación? (S/N): ").upper()
                if confirmar == 'S':
                    menu.pop(opcion - 1)
                    guardar_menu(menu)
                    print(f"Hot Dog '{nombre_hotdog}' eliminado del menú.")
                else:
                    print(f"Eliminación de Hot Dog '{nombre_hotdog}' cancelada.")

        else:
            print("Opción inválida.")
    except ValueError:
        print("Entrada inválida. Ingrese un número.")
mostrar_menu_hotdogs
def menu_gestion_hotdogs(inventario: Inventario, hotdogs_json: list):
    """Menú principal para la gestión de hot dogs usando datos remotos."""
    while True:
        print("\n==== Gestión del Menú de Hot Dogs ====")
        print("1. Ver la lista de hot dogs")
        print("2. Verificar inventario de un hot dog específico")
        print("3. Agregar un nuevo hot dog")
        print("4. Eliminar un hot dog existente")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_menu_hotdogs(hotdogs_json)

        elif opcion == "2":
            if not hotdogs_json:
                print("El menú está vacío.")
                continue
            
            print("\n=== Hot Dogs para Verificar ===")
            for i, item in enumerate(hotdogs_json, start=1):
                print(f"{i}. {item.get('nombre').upper()}")

            try:
                seleccion = int(input("Ingrese el número del Hot Dog a verificar: "))
                if 1 <= seleccion <= len(hotdogs_json):
                    verificar_inventario_hotdog(hotdogs_json[seleccion - 1], inventario)
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")

        elif opcion == "3":
            agregar_hotdog(inventario)
            hotdogs_json = cargar_menu()

        elif opcion == "4":
            eliminar_hotdog(inventario)
            hotdogs_json = cargar_menu()

        elif opcion == "5":
            break
        else:
            print("Opción no válida.")
