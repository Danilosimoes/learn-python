from banco_dados.bd import nova_conexao

sql = "SELECT * FROM contatos WHERE nome like 'lu%'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)