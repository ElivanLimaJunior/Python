import math
n1 = int(input('Digite um número '))
n2 = math.sqrt(n1)
print('O valor inteiro de {} é {} seu valor fracionado é de {:.2f} '.format(n1, math.ceil(n2), n2))

# irei arredondar agora para menos.

n3 = int(input('Digite um numero'))
n4 = math.sqrt(n3)
print('O valor inteiro de {} arredondado para baixo é {} seu valor fracionado é de {:.2f}'.format(n3, math.floor(n4), n4))




# criando um programa que leia o numero digitado e traga o valor inteiro dele.
# a função Trunc serve para eliminar todos os numeros dps da virgula.
from math import trunc
a1 = float(input('Digite um numero '))
print(' O numero inteiro de {} é {}'.format(a1, trunc(a1)))

# também funciona com a função 'int'
a2 = float(input('Digite um valor'))
print('O valor inteiro é {} e fracionado é {}'.format(a2, int(a2)))



