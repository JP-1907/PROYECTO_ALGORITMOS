class Cliente:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def __str__(self):
        return f"Cliente: {self.nombre} - Cédula: {self.cedula} - Edad: {self.edad}"

#Como ven tiene un solo método.
#¿Qué podría añadirse al enunciado para que cliente tenga más métodos?
#CRUD, Crear, Leer, Actualizar, Eliminar.