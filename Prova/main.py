from person import Person
from hobby import Hobby
from friend import Friend
from nuisance import Nuisance
from telemarketing import Telemarketing
from mosquito import Mosquito
from insect import Insect
from butterfly import Butterfly

print('\nPERSON')
p1 = Person('Chloe', 24)
print(p1)
print(p1.validaIdade())

print('\n----------------------------')

print('\nHOBBY')
h1 = Hobby.sports
print(h1.my_hobby())

print('\n----------------------------')

print('FRIEND')
f1 = Friend('Valeria', 18, 'games')
print(f1)
print(f1.chill())

print('\n----------------------------')

print('\nINSECT')
ins = Insect('Wasp')
print(ins)

print('\n----------------------------')

print('Telemarketing')
t1 = Telemarketing('Demetrios', 25)
print(t1.annoy())
print(t1.giveSalesPitch())

print('\n----------------------------')

print('\nMOSQUITO')
m1 = Mosquito('Culex tarsalis')
print(m1.buzz())
print(m1.annoy())

print('\n----------------------------')

print('\nBUTTERFLY')
b1 = Butterfly('Morpho', 'laranja, Azul, branco',)
print(b1)

print('\n----------------------------')

Nuisance.register(Telemarketing)

amg1 = Friend("Michael", 22, "jogar")
amg2 = Friend("Iara", 19, "caminhar")
amg3 = Friend("Duda", 19, "falar")

if amg2.__eq__(amg1): 
    print("Amigos iguais")
else:
    print("Amigos diferentes")

if amg1.__eq__(amg3): 
    print("Amigos iguais")
else:
    print("Amigos diferentes")
