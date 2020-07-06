pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Artur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

nome_maior = filter(lambda p: len(p['nome']) > 6, pessoas)
print(tuple(nome_maior))

totais = tuple(
    map(
        lambda total: total['idade'], pessoas
    )
)
print(sum(totais))
