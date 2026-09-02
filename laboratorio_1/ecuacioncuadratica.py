import math


class EcuacionCuadratica:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b ** 2 - 4 * self.a * self.c

    def getRaiz1(self):
        discriminante = self.getDiscriminante()

        if discriminante >= 0:
            return (-self.b + math.sqrt(discriminante)) / (2 * self.a)
        else:
            return 0

    def getRaiz2(self):
        discriminante = self.getDiscriminante()

        if discriminante >= 0:
            return (-self.b - math.sqrt(discriminante)) / (2 * self.a)
        else:
            return 0


# Programa de prueba
a, b, c = map(float, input("Ingrese a, b, c: ").split())

ecuacion = EcuacionCuadratica(a, b, c)

discriminante = ecuacion.getDiscriminante()

if discriminante > 0:
    print("La ecuación tiene dos raíces",
          ecuacion.getRaiz1(), "y", ecuacion.getRaiz2())

elif discriminante == 0:
    print("La ecuación tiene una raíz", ecuacion.getRaiz1())

else:
    print("La ecuación no tiene raíces reales")