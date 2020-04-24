import math

numberOne = 0
numero2 = 0
operacao = ''

numberOne = int(input('Digite  numero 1: '))
operacao = input('Digite a operação: ')
numero2 = int(input('Digite  numero 2: '))

if operacao == '+':
    resultado = numberOne + numero2
elif operacao == '-':
    resultado = numberOne - numero2
elif operacao == '*':
    resultado = numberOne * numero2
elif operacao == '/':
    resultado = numberOne / numero2
else:
    resultado = 'Operação inválida'

print(str(numberOne) + str(operacao) + '' + str(numero2) + '=' + str(resultado))
print(f"{numberOne} {operacao} {numero2} = {resultado}")
