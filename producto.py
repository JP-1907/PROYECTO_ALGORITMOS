class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio:.2f} - Cantidad: {self.cantidad}"

class Postre(Producto):
    def __init__(self, id, nombre, precio, cantidad, es_vegano):
        super().__init__(id, nombre, precio, cantidad)
        self.es_vegano = es_vegano

class Cafe(Producto):
    def __init__(self, id, nombre, precio, cantidad, tamaño, es_descafeinado):
        super().__init__(id, nombre, precio, cantidad)
        self.tamaño = tamaño
        self.es_descafeinado = es_descafeinado

class Jugo(Producto):
    def __init__(self, id, nombre, precio, cantidad, sabor, contiene_azucar):
        super().__init__(id, nombre, precio, cantidad)
        self.sabor = sabor
        self.contiene_azucar = contiene_azucar

    def es_saludable(self):
        return not self.contiene_azucar