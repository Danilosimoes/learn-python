# dado personalizado
class Data:
    def __init__(self, dia=1, mes=2, ano=1970):
        # init chama um objeto
        # os parametros são definidos aqui
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        # o self te que estar explicito o objeto em execução
        # self é o objto que está em execução
        return f'{self.dia}/{self.mes}/{self.ano}'


# instânciar, a partir de uma classe criar um objeto
d1 = Data(ano=2020)
# ao ver um codigo terminado entre parenteses, qur dizer que esta camando uma função ou metodo
# nesse caso é um método especial, é um construtor
# o construtor faz a ponte entre a classe e o objeto gerado

d1.dia = 5
# d1.mes = 12
# d1.ano = 2020
print(d1)
# ao usar o __str__ não precisa do nome da função, pode usar somente o d1
# converte o objeto pra string
# o self é o d1
# aqui o o python não exige que vc passe o objeto quando chama a função
# foi chamado ao usar o ponto
# usar o ponto pra acessar os membros de um objeto.
# tanto pra atribuir um atributo como no caso do d1 e d2.
# quanto no caso pra acessar funcionalidades no .to_str (comportamentos associados)


d2 = Data(dia = 12)
# d2.dia = 7
# d2.mes = 11
d2.ano = 2020
print(d2)

''' ao definir a função init, teve que dar posição aos elemntos, pois ele pedia 3
    e comentar as linhas, aonde estavam definidos os (d1 e d2), pois não eram posicionais'''

''' os padrões podem ser aleterados, como voce definindo o objeto'''

'''Construtores de objeto foi visto aqui também, os objetos são importantes,
a paritr deles são construidas as instâncias dos objetos, ao chamar o objeto,
é pelo nome da classe'''
# há varias formas diferentes de chamar o construtor, como fiz no exemplo acima
# pode ser passado parametros nomeados, posicionais, e tbm não passar nenhum
# depende da configuração
