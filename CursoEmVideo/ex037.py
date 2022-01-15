n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O número {} é maior que o {}'.format(n1,n2))
elif n2 > n1:
    print('{} é menor que {}'.format(n1,n2))
else:
    print('Os valores são iguais')
