from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador escolher um numero de 0 a 5
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print('-=-' * 20)
contagem = 0
jogador = False
while not jogador:
    jogador1 = int(input('Digite um número:  '))  # Número para adivinhar
    print('PROCESSANDO...')
    contagem += 1
    sleep(1)
    if jogador1 == computador:
        print('\nPARABENS VOCÊ ACERTOU')
        print('N° de tentativas: {}.'.format(contagem))
        jogador = True
    else:
        if jogador1 < computador:
            print('Mais... Tente novamente!')
        elif jogador1 > computador:
            print('Menos... Tente novamente!')
print('Fim')