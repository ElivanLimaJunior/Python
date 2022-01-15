cont = 0
n = int(input('Quer ver a tabuada de qual número? '))
while True:
    cont += 1
    if cont > 10:
        print('-'*50)
        n = int(input('Quer ver a tabuada de qual número? '))
        print('-'*50)
        cont = 1
    if n < 0:
        break
    soma = n * cont
    print(f'{n} x {cont} = {soma}')
print('-'*50)
print('Fim')
