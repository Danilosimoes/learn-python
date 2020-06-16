def get_tipo_dia(dia):
    dias = {
        1: 'Final de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Final de semana',

    }
    return dias.get(dia, '**dia invalido**')


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: {get_tipo_dia(dia)}')
