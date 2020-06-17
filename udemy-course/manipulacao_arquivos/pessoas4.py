try:
    arquivo = open('people.csv')


    for registro in arquivo:
        print('Nome: {} Idade: {} Estado: {}'.format(*registro.strip().split(',')))

finally:
    arquivo.close()

if arquivo.close():
    print('Arquivo ja foi fechado!')
