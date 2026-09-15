import math

class Fraccion:
    def __init__(self, a=0, b=1):
        self.numerador = a
        self.denominador = b

    def __add__(self, o):
        a = self.numerador * o.denominador + self.denominador * o.numerador
        b = self.denominador * o.denominador
        return Fraccion(a, b)

    def __sub__(self, o):
        a = self.numerador * o.denominador - self.denominador * o.numerador
        b = self.denominador * o.denominador
        return Fraccion(a, b)

    # 1. Multiplicación (a/b * c/d)
    def __mul__(self, o):
        a = self.numerador * o.numerador
        b = self.denominador * o.denominador
        return Fraccion(a, b)

    # 2. División (a/b / c/d)
    def __truediv__(self, o):
        a = self.numerador * o.denominador
        b = self.denominador * o.numerador
        return Fraccion(a, b)

    # 3. Igualdad
    def __eq__(self, o):
        if not isinstance(o, Fraccion):
            return False
        return self.numerador * o.denominador == self.denominador * o.numerador

    # 4. Convertir a decimal (validando división entre 0)
    def convertirADecimal(self):
        if self.denominador == 0:
            print("Error: división entre cero")
            return 0.0
        return self.numerador / self.denominador

    # 5. Comprobar si es inverso (a * b == 1)
    def esInverso(self, o):
        res = self * o
        return res.convertirADecimal() == 1.0

    # 6. parseFraccion
    def parseFraccion(self, cadena):
        partes = cadena.split("/")
        num = int(partes[0])
        den = int(partes[1])
        return Fraccion(num, den)

    # 7. Simplificar fracción
    def simplifica(self):
        mcd = math.gcd(self.numerador, self.denominador)
        num = self.numerador // mcd
        den = self.denominador // mcd
        return Fraccion(num, den)

    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)


# --- PRUEBAS DEL EJERCICIO 1 ---
f1 = Fraccion(1, 4)
f2 = Fraccion(4, 3)

print("f1 =", f1)
print("f2 =", f2)
print("Suma (f1 + f2):", f1 + f2)
print("Resta (f1 - f2):", f1 - f2)
print("Multiplicación (f1 * f2):", f1 * f2)
print("División (f1 / f2):", f1 / f2)
print("¿f1 es igual a f2?:", f1 == f2)
print("Decimal de f1:", f1.convertirADecimal())
print("¿f1 es inverso de (4/1)?:", f1.esInverso(Fraccion(4, 1)))

# Prueba de parseFraccion y simplifica
f_aux = Fraccion(0, 1)
f_parsed = f_aux.parseFraccion("-2/3")
print("parseFraccion('-2/3'):", f_parsed)
print("Simplificación de 2/8:", Fraccion(2, 8).simplifica())