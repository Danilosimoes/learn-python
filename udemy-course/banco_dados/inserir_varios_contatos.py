from mysql.connector.errors import ProgrammingError
from banco_dados.bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ga', '98765-4321'),
    ('Bia', '98765-8945'),
    ('Edu', '98456-8745'),
    ('Dan', '99632-1478'),
    ('Lis', '93215-8954'),
    ('Pedro', '98789-2258'),
    ('La', '95678-4321'),
)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')