t2 = 1
t3 = 1
cont = 1
quant = int(input('Quantos termos você quer ver ? '))
print('~'*20)
quant -= 1
print('0, 1, ', end='')
while quant != cont:
    t4 = t3
    print('{}, '.format(t4), end='')
    t3 = t3 + t2
    t2 = t4
    cont += 1
print('Fim')
print('~'*20)
