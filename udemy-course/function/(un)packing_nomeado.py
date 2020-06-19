# **kwargs
def resultado_f1(**podium):  # ** retorna um dict
    for posicao, piloto in podium.items():  # .items percorre chave e valor
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='L. Hmailton',  # parametros nomeados
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')
# packing nomeado, pegando os elemento, transformando em dict e jogando dentro da função


# Other way

def podio_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


if __name__ == '__main__':
    classificacao = {'segundo': 'M. Verstappen',
                     'primeiro': 'L. Hamilton',
                     'terceiro': 'S. Vettel'}
    podio_f1(**classificacao)


# unpacking