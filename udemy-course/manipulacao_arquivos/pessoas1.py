arquivo = open('people.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print('Nome: {}, Idade: {}, Estado: {}'. format(*registro.split(',')) )

