# inventario.py

# inventario.py

from producto import Producto, Pan, Refresco, PerroProducto
from typing import List, Optional

class Inventario:
    def __init__(self, productos: List[Producto]):
        self.productos: List[Producto] = productos
        self._productos_por_id = {p.id: p for p in productos}
    
    def visualizar_inventario(self):
        print("\n==== Inventario Completo ====")
        if not self.productos:
            print("El inventario está vacío.")
            return
        for producto in self.productos:
            print(f"ID: {producto.id}. {producto.nombre} - Cantidad en stock: {producto.cantidad}")
        print("---------------------------------")

    def buscar_existencia_por_nombre(self, nombre_producto: str) -> Optional[Producto]:
        nombre_lower = nombre_producto.lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_lower:
                print(f"\nProducto encontrado: {producto.nombre} - Cantidad en stock: {producto.cantidad}")
                return producto
        print(f"\nProducto '{nombre_producto}' no encontrado en el inventario.")
        return None

    def buscar_existencia_por_id(self, id_producto: int) -> Optional[Producto]:
        producto = self._productos_por_id.get(id_producto)
        if producto:
            print(f"\nProducto encontrado: {producto.nombre} - Cantidad en stock: {producto.cantidad}")
            return producto
        print(f"\nProducto con ID {id_producto} no encontrado en el inventario.")
        return None

    def listar_por_categoria(self, tipo_clase):
        print(f"\n==== Stock de Categoría: {tipo_clase.__name__} ====")
        encontrados = False
        for producto in self.productos:
            if isinstance(producto, tipo_clase):
                print(f"ID: {producto.id}. {producto.nombre} - Cantidad en stock: {producto.cantidad}")
                encontrados = True
        if not encontrados:
            print(f"No hay productos de la categoría '{tipo_clase.__name__}' en el inventario.")
        print("---------------------------------")

    def actualizar_existencia(self, id_producto: int, nueva_cantidad: int) -> bool:
        if nueva_cantidad < 0:
            print("La cantidad en stock no puede ser negativa.")
            return False
        producto = self._productos_por_id.get(id_producto)
        if producto:
            producto.cantidad = nueva_cantidad
            print(f"\nStock actualizado para {producto.nombre}. Nueva cantidad: {producto.cantidad}")
            return True
        else:
            print(f"\nNo se puede actualizar: Producto con ID {id_producto} no encontrado.")


