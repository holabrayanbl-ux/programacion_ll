import math

class Vector3D:
    def __init__(self, a1=0.0, a2=0.0, a3=0.0):
        self.a1 = float(a1)
        self.a2 = float(a2)
        self.a3 = float(a3)

    # a) Suma
    def __add__(self, b):
        return Vector3D(self.a1 + b.a1, self.a2 + b.a2, self.a3 + b.a3)

    # Resta auxiliar
    def __sub__(self, b):
        return Vector3D(self.a1 - b.a1, self.a2 - b.a2, self.a3 - b.a3)

    # b) Multiplicación por escalar: r * a
    def mult_escalar(self, r):
        return Vector3D(r * self.a1, r * self.a2, r * self.a3)

    # c) Longitud del vector: |a|
    def longitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)

    # d) Normal del vector: a / |a|
    def normal(self):
        l = self.longitud()
        if l == 0:
            print("Error: Vector nulo")
            return Vector3D(0, 0, 0)
        return Vector3D(self.a1 / l, self.a2 / l, self.a3 / l)

    # e) Producto escalar: a . b
    def prod_escalar(self, b):
        return self.a1 * b.a1 + self.a2 * b.a2 + self.a3 * b.a3

    # f) Producto vectorial: a x b
    def prod_vectorial(self, b):
        x = self.a2 * b.a3 - self.a3 * b.a2
        y = self.a3 * b.a1 - self.a1 * b.a3
        z = self.a1 * b.a2 - self.a2 * b.a1
        return Vector3D(x, y, z)

    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"


class AlgebraVectorial:
    # a) Perpendicular: |a+b| = |a-b|
    def perp_a(self, a, b):
        return math.isclose((a + b).longitud(), (a - b).longitud())

    # b) Perpendicular: |a-b| = |b-a|
    def perp_b(self, a, b):
        return math.isclose((a - b).longitud(), (b - a).longitud())

    # c) Perpendicular: a . b = 0
    def perp_c(self, a, b):
        return math.isclose(a.prod_escalar(b), 0.0)

    # d) Perpendicular: |a+b|^2 = |a|^2 + |b|^2
    def perp_d(self, a, b):
        izq = (a + b).longitud() ** 2
        der = (a.longitud() ** 2) + (b.longitud() ** 2)
        return math.isclose(izq, der)

    # e) Paralela: a = r * b
    def paralela_e(self, a, b):
        if b.a1 != 0:
            r = a.a1 / b.a1
        elif b.a2 != 0:
            r = a.a2 / b.a2
        else:
            r = a.a3 / b.a3
        comp = b.mult_escalar(r)
        return math.isclose(a.a1, comp.a1) and math.isclose(a.a2, comp.a2) and math.isclose(a.a3, comp.a3)

    # f) Paralela: a x b = 0
    def paralela_f(self, a, b):
        return math.isclose(a.prod_vectorial(b).longitud(), 0.0)

    # g) Proyección de a sobre b
    def proyeccion_de_a_sobre_b(self, a, b):
        num = a.prod_escalar(b)
        den = b.longitud() ** 2
        return b.mult_escalar(num / den)

    # h) Componente de a en b
    def componente_de_a_en_b(self, a, b):
        return a.prod_escalar(b) / b.longitud()


# --- PRUEBAS DEL EJERCICIO 3 ---
v1 = Vector3D(3, 4, 0)
v2 = Vector3D(1, 0, 0)
alg = AlgebraVectorial()

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Suma (v1 + v2):", v1 + v2)
print("Escalar (2 * v1):", v1.mult_escalar(2))
print("Longitud v1:", v1.longitud())
print("Normal de v1:", v1.normal())
print("Producto escalar (v1 . v2):", v1.prod_escalar(v2))
print("Producto vectorial (v1 x v2):", v1.prod_vectorial(v2))

print("\n--- Pruebas de AlgebraVectorial ---")
print("¿Perpendicular C (a.b=0)?:", alg.perp_c(v1, v2))
print("¿Paralela F (axb=0)?:", alg.paralela_f(v1, Vector3D(6, 8, 0)))
print("Proyección de v1 sobre v2:", alg.proyeccion_de_a_sobre_b(v1, v2))
print("Componente de v1 en v2:", alg.componente_de_a_en_b(v1, v2))