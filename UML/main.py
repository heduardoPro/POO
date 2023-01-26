from uml import Ator, Aluno, Personagem, datetime

comeco = datetime(2020, 5, 17)
fim = datetime(2023, 1, 1)
salario = 6000

ator = Ator('Miguel', 'M', datetime(1978, 1, 1), comeco, fim, salario)
aluno = Aluno('Henrique', 'M', datetime(2002, 12, 15), 20221094040030)
personagem = Personagem('Eduur', 'M', datetime(1972, 2, 2), comeco, fim, salario, 'Parker', 'Homem-Aranha')

print(ator.get_nome())
print('-'*10)

print(aluno.get_nome())
print(aluno.get_matricula())
print('-'*10)

print(personagem.get_caracterizacao())
print(personagem.get_novela())
print(personagem.get_data_nasc())