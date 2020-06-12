#!/usr/bin/env python3


import math
import sys


def circulo(raio):
    return math.pi * float(raio) ** 2


if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)
    print(f'Ára do círculo {area}')