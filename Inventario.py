# inventario.py

# inventario.py

from producto import Producto, Pan, Refresco, PerroProducto
from typing import List, Optional

class Inventario:

    def __init__(self, productos: List[Producto]):
        # El inventario es una lista de objetos Producto (Pan, Refresco, etc.)
        self.productos: List[Producto] = productos
        # Se puede usar un diccionario para un acceso más rápido por ID
        self._productos_por_id = {p.id: p for p in productos}
    
    # 1. Visualizar todo el inventario
    def visualizar_inventario(self):

        print("\n==== 📋 Inventario Completo ====")
        if not self.productos:
            print("El inventario está vacío.")
            return

        for producto in self.productos:
            print(f"ID: {producto.id}. {producto.nombre} - Cantidad en stock: {producto.cantidad}")
        print("---------------------------------")

    # 2. Buscar la existencia de un ingrediente específico
    def buscar_existencia_por_nombre(self, nombre_producto: str) -> Optional[Producto]:

        nombre_lower = nombre_producto.lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_lower:
                print(f"\n🔍 Producto encontrado: {producto.nombre} - Cantidad en stock: {producto.cantidad}")
                return producto
        print(f"\n Producto '{nombre_producto}' no encontrado en el inventario.")
        return None

    def buscar_existencia_por_id(self, id_producto: int) -> Optional[Producto]:


        producto = self._productos_por_id.get(id_producto)
        if producto:
            print(f"\n🔍 Producto encontrado: {producto.nombre} - Cantidad en stock: {producto.cantidad}")
            return producto
        print(f"\n Producto con ID {id_producto} no encontrado en el inventario.")
        return None

    # 3. Listar las existencias de todos los ingredientes de una categoría
    def listar_por_categoria(self, tipo_clase):

        print(f"\n====  Stock de Categoría: {tipo_clase.__name__} ====")
        encontrados = False
        for producto in self.productos:
            if isinstance(producto, tipo_clase):
                print(f"ID: {producto.id}. {producto.nombre} - Cantidad en stock: {producto.cantidad}")
                encontrados = True
        
        if not encontrados:
            print(f"No hay productos de la categoría '{tipo_clase.__name__}' en el inventario.")
        print("---------------------------------")


    # 4. Actualizar la existencia de un producto específico
    def actualizar_existencia(self, id_producto: int, nueva_cantidad: int) -> bool:

        if nueva_cantidad < 0:
            print(" La cantidad en stock no puede ser negativa.")
            return False
            
        producto = self._productos_por_id.get(id_producto)
        
        if producto:
            # Opción para actualizar completamente:
            producto.cantidad = nueva_cantidad
            # Si se quisiera *agregar* una cantidad, sería: producto.cantidad += cantidad_a_agregar
            print(f"\n Stock actualizado para {producto.nombre}. Nueva cantidad: {producto.cantidad}")
            return True
        else:
            print(f"\n No se puede actualizar: Producto con ID {id_producto} no encontrado.")
            return False
