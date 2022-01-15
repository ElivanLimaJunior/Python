print('A cotação do dolar nesse determinado momento está 5.21 U$')
n2 = float(input('Digite o valor que que tem em sua carteira: R$ '))
dolar = float('5.24')
a = n2 / dolar
b = bool('{}'.format(a))
print('Com {:.2f} Reais você consegue comprar {:.2f} dolares'.format(n2, a))

