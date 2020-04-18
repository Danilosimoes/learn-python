preço = float(input('Qual o valor consumido? R$'))
novo = preço + (preço * 10 / 100)
print('O cliente gastou no ComaBem R${:.2f}, com os 10% do garçom o valor vai ficar R${:.2f}'.format(preço, novo))
