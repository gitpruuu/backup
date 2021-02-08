class Programa():
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return(f'Nome: {self.nome} Likes: {self.likes}')

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return(f'Nome {self.nome} Likes: {self.likes}')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return(f'Nome: {self.nome} Likes: {self.likes}')

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()

tmep = Filme('todo mundo em panico', 1999, 100)
tmep.dar_likes()
tmep.dar_likes()

demolidor = Serie('demolidor', 2016, 2)
demolidor.dar_likes()
demolidor.dar_likes()

lista = [atlanta, vingadores, tmep, demolidor]

minha_playlist = Playlist('fim de semana', lista)

try:
    for programa in minha_playlist:
        print(programa)
except TypeError as tp:
    print(f"Erro : {tp}")
finally:
    print(f'Tamanho: {len(minha_playlist)}')
