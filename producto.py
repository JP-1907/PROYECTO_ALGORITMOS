class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio:.2f} - Cantidad: {self.cantidad}"

class Perro:
    def __init__(self, nombre, pan, salchicha, toppings, salsas, acompañantes):
        self.nombre = nombre
        self.pan = pan
        self.salchicha = salchicha
        self.toppings = toppings
        self.salsas = salsas
        self.acompañantes = acompañantes
class PerroProducto(Producto):
    def __init__(self, id, nombre, precio, cantidad):
        super().__init__(id, nombre, precio, cantidad)
    def __str__(self):
        return f"{super().__str__()} - Tipo: {tipo}"
class Pan(Producto):
    def __init__(self, id, nombre, precio, cantidad, tamaño):
        super().__init__(id, nombre, precio, cantidad)
        self.tamaño = tamaño

class Refresco(Producto):
    def __init__(self, id, nombre, precio, cantidad):
        super().__init__(id, nombre, precio, cantidad)

    def es_saludable(self):

        return not self.contiene_azucar


