compras = (
    {'Quantidade': 2, 'Preço': 10},
    {'Quantidade': 3, 'Preço': 20},
    {'Quantidade': 5, 'Preço': 14},

)


def calc_preco_total(compra):
    return compra['Quantidade'] * compra['Preço']


totais = tuple(map(calc_preco_total, compras))

print('Preços totais', totais)
print('Total geral:', sum(totais))
