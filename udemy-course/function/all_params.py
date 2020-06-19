def todos_params(*args, **kwargs):  # parametros posicionais, parametros nomeados
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    todos_params('a', 'b', 'c')  # tupla(args)
    todos_params(1, 2, 3, legal=True, valor=12.99)  # nomeando params (tupla and dict)
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
# argumento nomeado depois do posicional
    todos_params(primeiro='João', segundo='Maria')
    todos_params('Maria', primeiro='João')
