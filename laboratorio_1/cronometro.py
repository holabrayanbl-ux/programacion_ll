import time
import random
class Cronometro:
    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = self.__inicia
    def get_inicia(self):
        return self.__inicia
    def get_finaliza(self):
        return self.__finaliza
    def inicia(self):
        self.__inicia = time.time()
    def detener(self):
        self.__finaliza = time.time()
    def lapso_de_tiempo(self):
        return (self.__finaliza - self.__inicia) * 1000
def ordenacion_seleccion(lista):
    """Algoritmo de Ordenación por Selección (Selection Sort)."""
    n = len(lista)
    for i in range(n - 1):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
if __name__ == "__main__":
    tamano = 100000
    print(f"Generando {tamano} números aleatorios...")
    numeros = [random.uniform(0, 100000) for _ in range(tamano)]
    cronometro = Cronometro()
    print("Iniciando la ordenación por selección...")
    cronometro.inicia()
    ordenacion_seleccion(numeros)
    cronometro.detener()
    print(f"Tiempo de ejecución: {cronometro.lapso_de_tiempo():.2f} ms")