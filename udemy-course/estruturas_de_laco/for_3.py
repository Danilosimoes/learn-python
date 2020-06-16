produto = {'Nome': 'Caneta Chic', 'Preço': 14.99,
           'Importada': True, 'Estoque': 793}

for key in produto:
    print(key)

for valor in produto.values():
    print(valor)

for key, valor in produto.items():
    print(key, '=', valor )

print(key, valor)