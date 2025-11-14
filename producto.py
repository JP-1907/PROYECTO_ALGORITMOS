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
    def __init__(self, id, nombre, precio, cantidad, tipo_salchicha="vienesa"):
        super().__init__(id, nombre, precio, cantidad)
        self.tipo_salchicha = tipo_salchicha

    def __str__(self):
        return 

    def __str__(self):
        return f"{super().__str__()} - Tipo de salchicha: {self.tipo_salchicha}"

class Pan(Producto):
    def __init__(self, id, nombre, precio, cantidad, tamaño):
        super().__init__(id, nombre, precio, cantidad)
        self.tamaño = tamaño

    def __str__(self):
        return f"{super().__str__()} - Tamaño: {self.tamaño}"




class Topping(Producto):
    def __init__(self, id, nombre, precio, cantidad, es_picante=False):
        super().__init__(id, nombre, precio, cantidad)
        self.es_picante = es_picante

    def __str__(self):
        picante = "Picante" if self.es_picante else "No picante"
        return f"{super().__str__()} - {picante}"

class Salsa(Producto):
    def __init__(self, id, nombre, precio, cantidad, tipo="cremosa"):
        super().__init__(id, nombre, precio, cantidad)
        self.tipo = tipo 

    def __str__(self):
        return f"{super().__str__()} - Tipo de salsa: {self.tipo}"

class Acompañamiento(Producto):
    def __init__(self, id, nombre, precio, cantidad, tipo="bebida", detalles=None):
        super().__init__(id, nombre, precio, cantidad)
        self.tipo = tipo  # Ejemplo: bebida, papas, jugo, postre
        self.detalles = detalles if detalles else []  # Ejemplo: ["limón", "hielo"]

    def __str__(self):
        detalles_str = ", ".join(self.detalles) if self.detalles else "Sin detalles"
        return f"{super().__str__()} - Tipo: {self.tipo} - Detalles: {detalles_str}"






