

with open('people.csv') as arquivo:
    with open('people.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {} Idade: {} Estado: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo ja foi fechado!')

if saida.closed:
    print('Arquivo de saída já foi fechado!')
