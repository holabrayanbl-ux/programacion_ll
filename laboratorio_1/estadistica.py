import math


class Estadistica:

    def __init__(self, valores):
        self.valores = valores

    def promedio(self):
        return sum(self.valores) / len(self.valores)

    def desviacion(self):
        media = self.promedio()
        suma = 0

        for x in self.valores:
            suma += (x - media) ** 2

        return math.sqrt(suma / (len(self.valores) - 1))


# Programa de prueba
numeros = list(map(float, input("Ingrese 10 números: ").split()))

estadistica = Estadistica(numeros)

print("El promedio es", estadistica.promedio())
print("La desviación estandard es", estadistica.desviacion())