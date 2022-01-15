from time import sleep
print('{:~^40}'.format('A Queima de Fogos Já Vai Começar!'))
print('Contagem Regressiva:')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('Fim')
