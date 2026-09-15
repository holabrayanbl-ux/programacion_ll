import math

class MiPunto:
    # a), b) y c) Atributos, getters y constructores (con y sin argumentos)
    def __init__(self, x=0.0, y=0.0):
        self._x = float(x)
        self._y = float(y)

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    # d) y e) Método distancia sobrecargado (recibe 1 objeto o 2 números x, y)
    def distancia(self, *args):
        if len(args) == 1:
            ox = args[0].getX()
            oy = args[0].getY()
        else:
            ox = float(args[0])
            oy = float(args[1])
        
        dx = self._x - ox
        dy = self._y - oy
        return math.sqrt(dx**2 + dy**2)


# --- PRUEBAS DEL EJERCICIO 2 ---
p1 = MiPunto(0, 0)
p2 = MiPunto(10, 30.5)

print("Punto 1:", p1.getX(), ",", p1.getY())
print("Punto 2:", p2.getX(), ",", p2.getY())
print("Distancia (pasando objeto):", p1.distancia(p2))
print("Distancia (pasando coordenadas x, y):", p1.distancia(10, 30.5))