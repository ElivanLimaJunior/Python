'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

''' Comecei a usar as novas FSTRING'''

soma = 0
cont = 0
o = 's'
while o != 'N': # Também pode ser usado: while o in 'Nn':
    n1 = int(input('Digite um número: '))
    soma += n1
    cont += 1
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
                menor = n1
    o = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior número foi {maior} e o menor foi {menor}.')
