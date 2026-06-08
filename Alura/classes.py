
class Restaurante:
    restaurante = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurante.append(self)
    def __str__(self):
        return f'{self.nome} - {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurante:
            print(f'{restaurante.nome.ljust(25)} - {restaurante.categoria.ljust(25)} - {restaurante.ativo}')

    def ativar(self):
        return 'Verdadeiro' if self.ativo == True else 'False'
restaurante_praca = Restaurante('Praca', 'Comida Caseira')
restaurante_pizza = Restaurante('Pizza Express', 'Pizzaria')

Restaurante.listar_restaurantes()

'''
class Musica:
    musica = []
    def __init__(self,nome,artista,duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musica.append(self)
    def __str__(self):
        return f' {self.nome} - {self.artista} - {self.duracao}'
    def listar_musicas():
        for musica in Musica.musica:
            print(f'{musica.nome} - {musica.artista} - {musica.duracao}')

musica1 = Musica("Bohemian Rhapsody", "Queen", 354)

musica2 = Musica("Imagine", "John Lennon", 183)
musica2.nome = "Imagine"
musica2.artista = "John Lennon"
musica2.duracao = 183

Musica.listar_musicas()
'''
'''
class Pessoa: 
    pessoa = []
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        Pessoa.pessoa.append(self)
    def __str__(self):
        return f'{self.nome} - {self.idade} - {self.cidade}'
    def listar_pessoas():
        for pessoa in Pessoa.pessoa:
            print(f'{pessoa.nome} - {pessoa.idade} - {pessoa.cidade}')
    
pessoa1 = Pessoa('Enzo', 34, 'São Paulo')
pessoa2 = Pessoa('Maria', 28, 'Rio de Janeiro')

Pessoa.listar_pessoas()
'''