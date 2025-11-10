import cliente
from producto import Jugo, Postre, Cafe

class Factura:
    def __init__(self, cliente, productos_seleccionados):
        self.cliente = cliente
        self.productos_seleccionados = productos_seleccionados

    def calcular_descuento(self):
        total_descuento = 0

        if self.cliente.edad > 65:
            total_descuento += 0.15 * self.calcular_total_sin_descuento()

        if "a" in self.cliente.nombre.lower():
            for producto, cantidad in self.productos_seleccionados:
                if isinstance(producto, Postre) and producto.es_vegano:
                    total_descuento += 0.05 * cantidad * producto.precio

                if isinstance(producto, Jugo) and producto.es_saludable():
                    total_descuento += 0.05 * cantidad * producto.precio

        return total_descuento

    def calcular_total_sin_descuento(self):
        total = 0
        for producto, cantidad in self.productos_seleccionados:
            total += cantidad * producto.precio
        return total

    def mostrar_factura(self):
        print(f"Factura para: \n{self.cliente.__str__()}")
        print("---------------------------------")

        for producto, cantidad in self.productos_seleccionados:
            print(f"{producto.id}. {producto.nombre}: {producto.precio} x {cantidad} - Precio: {cantidad * producto.precio:.2f}")

        total_sin_descuento = self.calcular_total_sin_descuento()
        descuento = self.calcular_descuento()
        total_pagar = total_sin_descuento - descuento

        print(f"Subtotal: {total_sin_descuento:.2f}")
        print(f"Descuento: {descuento:.2f}")
        print(f"Total a pagar: {total_pagar:.2f}")
