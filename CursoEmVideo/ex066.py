''' Crie um programa que leia números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

soma = n = cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
                menor = n
print(f'A soma dos números é igual a {soma}')
print(f'O maior número é {maior} e o menor é {menor}')
print('Fim')
