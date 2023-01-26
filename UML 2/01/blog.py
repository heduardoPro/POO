import datetime

from postagem import Postagem

class Blog:

    postagens: Postagem = []

    def __init__(self, nome_blog: str) -> None:
        self.nome_blog = nome_blog

    def __str__(self) -> str:
        return '{}'.format(self.nome_blog)

    def add_postagem(self, postagem):
        self.postagens.append(postagem)

    def publicar_postagem(self, postagem):
        print(postagem)

    def listar_postagens_publicadas(self):
        for i in Blog.postagens:
            if datetime.datetime.now() > i.data_publicacao:
                print(i)

    def listar_todas_as_postagens(self):
        for i in self.postagens:
            print(i.titulo)

    def apagar_postagem(self, postagem: Postagem):
        for i in self.postagens:
            if i == postagem:
                self.postagens.remove(i)
