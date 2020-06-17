

with open('people.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {} Idade: {} Estado: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo ja foi fechado!')
