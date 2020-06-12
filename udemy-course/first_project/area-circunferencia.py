import math
import sys


def circulo(raio):
    return math.pi * float(raio) ** 2


if __name__ == '__main__':
    raio = float(input("Digite o raio: "))
    area = circulo(raio)
    print('Ára do círculo', area)