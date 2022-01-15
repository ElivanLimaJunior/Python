# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um
# número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador escolher um numero de 0 a 5
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Digite um número:  ')) # Número para adivinhar
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABENS VOCÊ ACERTOU')
else:
    print('Eu ganhei! Eu pensei no número {} e não no {}.'.format(computador, jogador))
