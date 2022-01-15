# Faça um programa que leia um número de 0 a 9999 e mostre na tabela cada um dos digitos separados.
#EX: Digite um número: 1834 = unidade: 4 dezena: 3 centena: 8 milhar: 1

n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('{} milhares.'.format(n2[1]))
print('{} centenas. '.format(n2[2]))
print('{} dezenas. '.format(n2[3]))
print('{} unidades.'.format(n2[4]))

numero = str(input("Digite um numero de 1 a 9999: "))
print("A casa do milhar vale:, ", numero[0])
print("A casa da centena vale: ", numero[1])
print("A casa da dezena vale: ", numero[2])
print("A casa da unidade vale: ", numero[3])
