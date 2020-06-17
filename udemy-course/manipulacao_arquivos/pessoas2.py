arquivo = open('people.csv')
for registro in arquivo:
    print('Nome: {} Idade: {} Estado: {}'.format(*registro.split(',')))
arquivo.close()


