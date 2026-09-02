import math
def promedio(numeros):
    suma = 0

    for numero in numeros:
        suma = suma + numero

    return suma / len(numeros)

def desviacion(numeros):
    media = promedio(numeros)
    suma = 0

    for numero in numeros:
        suma = suma + (numero - media) ** 2

    return math.sqrt(suma / (len(numeros) - 1))

numeros = []

print("Ingrese 10 números:")

for i in range(10):
    numero = float(input())
    numeros.append(numero)

media = promedio(numeros)
desviacion_estandar = desviacion(numeros)

print("El promedio es", media)
print("La desviación estandard es", desviacion_estandar)