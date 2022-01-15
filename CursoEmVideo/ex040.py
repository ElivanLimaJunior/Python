n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
média = (n1+n2) / 2
if média < 5.0:
    print('sua média é {}, você está \033[1;31mReprovado\033[m'.format(média))
elif média < 7.0:
    print('Sua média é {}, você está em \033[1;32mRecuperação\033[m'.format(média))
else:
    print('Sua média é {}, \n\033[1;35mParabéns!!! Você está APROVADO!\033[m'.format(média))