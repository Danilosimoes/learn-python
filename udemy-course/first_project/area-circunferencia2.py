import math
import sys

def circulo(raio):
    return math.pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("É necessario informar o raio do circulo.")
        print("Sintaxe: {} <raio>".format(sys.argv[0]))
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(f'Ára do círculo {area}')

