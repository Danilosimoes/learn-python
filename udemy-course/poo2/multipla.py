class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class HomemAranha(Aranha, Homem):
    @property
    def capacidades(self):
        return super().capacidades + \
               ('bater em bandidos', 'atirar teias em prédios')


if __name__ == '__main__':
    john = Homem()
    print(f'john: {john.capacidades}')

    aranha = Aranha()
    print(f'Aranha: {aranha.capacidades}')


    peter = HomemAranha()
    print(f'Peter Parker: {peter.capacidades}')