# Lista de Convidados

lista_convidados = input('Coloque o número de convidados: ')
convidados = []

i = 1
while i <= int(lista_convidados):
    nome_do_convidado = input('Coloque o nome do convidado #'+ str(i) +': ')
    convidados.append(nome_do_convidado)
    i += 1

print('Serão', lista_convidados, 'convidados')
print('\nLISTA DE CONVIDADOS')
print('######################')

for convidado in convidados:
    print(convidado)