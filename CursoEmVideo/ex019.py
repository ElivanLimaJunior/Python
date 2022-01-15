import random
n1 = str(input('Primeiro Aluno '))
n2 = str(input('Segundo Aluno '))
n3 = str(input('Terceiro Aluno '))
n4 = str(input('Quarto Aluno '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O escolhido foi {} '.format(escolhido))

# ou importando da biblioteca apenas a função choice
# com isso na primeira linha iria ficar "from random import choice" e na linha 7 "escolhido = choice.(lista)

