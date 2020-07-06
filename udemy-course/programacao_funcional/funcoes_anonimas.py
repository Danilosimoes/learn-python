compras = (
    {'Quantidade': 2, 'Preço': 10},
    {'Quantidade': 3, 'Preço': 20},
    {'Quantidade': 5, 'Preço': 14},

)

totais = tuple(
    map(
        lambda compra: compra['Quantidade'] * compra['Preço'],
        compras

    )

)

print('Preços totais', totais)
print('Total geral:', sum(totais))
