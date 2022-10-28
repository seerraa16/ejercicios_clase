class Punto:
    """Representa un punto en el espacio"""

    def __init__(self, x, y, z):
        """Método de inicialización de un punto en el espacio"""
        self.x = x
        self.y = y
        self.z = z

    def mostrar(self):
        """Método temporal utilizado para mostrar nuestro punto"""
        print("Punto ({}, {}, {})".format(self.x, self.y, self.z))


p = Punto(1, 2, 3)
p.mostrar()

