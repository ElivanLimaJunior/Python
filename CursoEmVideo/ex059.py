# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))

contador = 1
while contador != 0:
    opção = int(input('''Escolha uma das opções
    [ 1 ] Soma.
    [ 2 ] Multiplicação.
    [ 3 ] Maior.
    [ 4 ] Novos números.
    [ 5 ] Fim do Programa.
    '''))
    if opção == 1:
        soma = primeiro + segundo
        print('A soma dos dois números é igual a {}.'.format(soma))
    elif opção == 2:
        mult = primeiro * segundo
        print('A multiplicação dos números é igual a {}.'.format(mult))
    elif opção == 3:
        if primeiro >= segundo:
            maior = primeiro
            print('O maior número é {}.'.format(maior))
        else:
            maior = segundo
            print('O maior número é {}.'.format(maior))
    elif opção == 4:
        print('Insira 2 novos números')
        primeiro = int(input('Primeiro número: '))
        segundo = int(input('Segundo número: '))
    elif opção == 5:
        contador = 0
    elif opção > 5:
        print('Opção inválida, digite novamente!\n')
        sleep(1)
    print('=-=' * 20)

print('Fim do Programa')
