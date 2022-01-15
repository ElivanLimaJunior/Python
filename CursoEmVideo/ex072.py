# Crie um programa que tenha umatupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.
while True:
    cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatoze', 'Quinze', 'Desesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
    n = int(input('Digite um número entre 0 e 20: '))
    while n > 20:
        print('\nVocê digitou um número invalido...\nPor favor, Tente novamente!\n')
        n = int(input('Digite um número entre 0 e 20: '))
    print(f'\nVocê digitou {cont[n]}')
    op = str(input('Deseja continuar ? [S/N] ')).upper().strip()
    if op == 'N':
        break