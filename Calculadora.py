import math
numero1 = 0
numero2 = 0
operacao = ''

numero1 = int(input('Digite  numero 1: '))
operacao = input('Digite a operação: ')
numero2 = int(input('Digite  numero 2: '))

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2
else:
    resultado = 'Operação inválida'

print(str(numero1) + str(operacao) + '' + str(numero2) + '=' + str(resultado))

