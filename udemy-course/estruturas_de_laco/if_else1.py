def faixa_etaria(idade):
    if 0 <= idade <18:
        return 'Menor de idade'
    elif idade in range(18, 64):
        return 'Adulto'
    elif idade in range(65, 99):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Idade Inválida'


if __name__ == '__main__':
    for idade in (17, 0, 37, 113, -2):
        print(f'{idade}: {faixa_etaria(idade)}')

if __name__ == '__main__':
    idade = int(input('Digite a idade: '))
    situacao = faixa_etaria(idade)
    print(situacao)
