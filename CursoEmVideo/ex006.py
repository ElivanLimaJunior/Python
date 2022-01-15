n1 = int(input('Digite um número: '))
a = n1*2
b = n1*3
c = n1**(1/2)
print('O dobro desse número é {} \nO triplo desse número é {} \nE a sua raiz quadrada é {:.2f}.'.format(a,b,c))

# Usando menos variaveis

n2 = int(input('\nDigite outro número: '))
print('O dobro vale {} o triplo vale {} e a sua raiz é {:.2f}.'.format((n2*2), (n2*3), (n2**(1/2) )))