import math
import sys
import errno

# !/Users/danil/PycharmProjects/Course/area-circunferencia3.py
def help():
    print("É necessario informar o raio do circulo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0]))


def circulo(raio):
    return math.pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    elif not sys.argv[1].isnumeric():
        print('O raio deve ser um valor numérico')
        sys.exit(errno.EINVAL)

    raio = float(sys.argv[1])
    area = circulo(raio)
    print(f'Área do círculo {area}')
