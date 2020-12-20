class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {(self.nome)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls, ):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 4


if __name__ == '__main__':
    gabriel = Mutante(nome='Gabriel')
    feliz = Homem(gabriel, nome='Feliz')
    print(Pessoa.cumprimentar(feliz))
    print(id(feliz))
    print(feliz.cumprimentar())
    print(feliz.nome)
    print(feliz.idade)
    for filho in feliz.filhos:
        print(filho.nome)
    feliz.olhos = 1
    del feliz.olhos
    print(gabriel.__dict__)
    print(feliz.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(feliz.olhos)
    print(gabriel.olhos)
    print(id(Pessoa.olhos), id(feliz.olhos), id(gabriel.olhos))
    print(Pessoa.metodo_estatico(), feliz.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), feliz.nome_e_atributo_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(gabriel, Pessoa))
    print(isinstance(gabriel, Homem))
    print(gabriel.olhos)
    print(feliz.cumprimentar())
    print(gabriel.cumprimentar())
