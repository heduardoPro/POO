from usuario import Usuario
from blog import Blog
from postagem import Postagem

user1 = Usuario(0, 'User01', 'admin01', '1234')
user2 = Usuario(1, 'User02', 'admin02', '1234')
user3 = Usuario(2, 'User03', 'admin03', '1234')

blog = Blog('Blog-PDF.com.br')
print(blog)

print('\nUltimas postagens')
postagem1 = Postagem(2023, 'PESSOA DESAPARECIDA EM PDF', 'JOVEM DESAPARECE APÓS SAIDA COM AMIGOS PARA BALADA', 2023, 1, 11, blog, user2)
postagem2 = Postagem(2022, 'AGERNTINA GANHA COPA DO MUNDO 2022', 'LIONEL MESSI GANHA SUA PRIMEIRA COPA AOS 36 ANOS', 2022, 12, 18, blog, user3)

blog.add_postagem(postagem1)
blog.add_postagem(postagem2)

blog.listar_postagens_publicadas()

print('-'*30)

blog.listar_todas_as_postagens()

print('-'*30)

blog.apagar_postagem(postagem2)
blog.listar_todas_as_postagens()