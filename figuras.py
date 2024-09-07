# Clase base Figura
class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_area(self):
        raise NotImplementedError("Este método debe ser implementado por cada figura.")

    def calcular_perimetro(self):
        raise NotImplementedError("Este método debe ser implementado por cada figura.")

# Clase Rectangulo
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        super().__init__("Rectángulo")
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

# Clase Circulo
import math

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Clase Cuadrado
class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

# Clase Triangulo
class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3):
        super().__init__("Triángulo")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"
