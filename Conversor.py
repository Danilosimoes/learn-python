dolar = float(input('Qual a cotação atual do dólar? US$ '))
real = float(input('Quantos reais você quer converter? R$ '))
conversao = real / dolar
print('Com o dolar custando US${} em reais você tem R${}'.format(dolar, conversao))
