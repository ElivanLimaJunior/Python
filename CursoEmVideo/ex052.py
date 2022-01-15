n1 = int(input('Digite um número: '))
tot = 0 # serve para fazer um contador. observe dentro da formula IF que ele está +1 para realizar a conta.
for c in range(1, n1+1, 1):
    if n1 % c == 0:
        print('\033[31m', end=' ')
        tot += 1 # += quer dizer que ele recebe ele mesmo EX: TOT = TOT + 1.
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} é divisivel {} vezes'.format(n1, tot))
if tot == 2:
    print('E por isso é um número \033[32mPRIMO\033[m')
else:
    print('E por isso ele \033[35mNÃO É PRIMO\033[m')
