from banco_dados.bd import nova_conexao
from mysql.connector import ProgrammingError

"""""
tabela_emails = '''
DROP TABLE emails
'''
"""
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('DROP TABLE emails')
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')