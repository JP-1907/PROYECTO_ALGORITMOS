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
    def __init__(self, id, nombre, precio, cantidad, es_vegano):
        super().__init__(id, nombre, precio, cantidad)
        self.es_vegano = es_vegano

    def __str__(self):
        tipo = "Vegano" if self.es_vegano else "No vegano"
        return f"{super().__str__()} - Tipo: {tipo}"
class Pan(Producto):
    def __init__(self, id, nombre, precio, cantidad, tamaño, es_integral):
        super().__init__(id, nombre, precio, cantidad)
        self.tamaño = tamaño
        self.es_integral = es_integral

class Refresco(Producto):
    def __init__(self, id, nombre, precio, cantidad, sabor, contiene_azucar):
        super().__init__(id, nombre, precio, cantidad)
        self.sabor = sabor
        self.contiene_azucar = contiene_azucar

    def es_saludable(self):

        return not self.contiene_azucar
