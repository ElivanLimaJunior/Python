n1 = float(input('Digite o preço do produto. '))
a = 5/100*n1
b= n1-a
print('Este produto está com o desconto de 5%, {:.2f} mas barato aproveite e leve por apenas {:.2f}!'.format(a, b))