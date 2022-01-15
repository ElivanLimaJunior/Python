import random
n1 = str(input('1° Aluno '))
n2 = str(input('2° Aluno '))
n3 = str(input('3° Aluno '))
n4 = str(input('4° Aluno '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A sequência será: ')
print(lista)

# agora importando apenas o shuffle
from random import shuffle
n5 = str(input('1 aluno '))
n6 = str(input('2 aluno '))
n7 = str(input('3 aluno '))
n8 = str(input('4 aluno '))
lista2 = [n5, n6, n7, n8]
shuffle(lista2)
print('Ordem será: ')
print(lista2)