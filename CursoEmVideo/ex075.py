# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os pares.

a = int(input('Digite um número: '))
b = int(input('Digite mais um número: '))
c = int(input('Digite outro número: '))
d = int(input('Digite o último número: '))
tupla = (a, b, c, d)
print(f'\nVocê digitou os valores {tupla}.')
print(f'O Valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1} posição.')
print('Os valores pares digitados foram... ',end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
