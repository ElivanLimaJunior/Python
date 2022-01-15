n1 = float(input('Primeiro numero '))
n2 = float(input('Segundo numero '))
n3 = float(input('Terceiro numero '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('É possivel formar um triangulo com esses valores')
else:
    print('Não é possivel formar um triangulo com esses valores')