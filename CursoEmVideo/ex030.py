n1 = int(input('Digite um número: '))
res = n1 % 2
print('O resultado é {}'.format(res))
if res == 1:
    print('{} é um número Impar!'.format(n1))
else:
    print('{} é um número Par'.format(n1))

# Outra maniera

n2 = int(input('Digite um número: '))%2
if 1:
    print('Este número Impar!'.format(n2))
else:
    print('Este número Par'.format(n2))