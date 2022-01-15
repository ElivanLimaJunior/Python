peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura: '))
imc = peso/altura**2
if imc < 18.5:
    print('Seu imc é de {:.1f}. \nVocê está abaixo do peso ideal'.format(imc))
elif imc < 25:
    print('Seu imc é de {:.1f}.\n\033[1;34mParabéns!! Você está no peso Ideal\033[m'.format(imc))
elif imc < 30:
    print('Seu imc é de {:.1f}.\nParece que você está com \033[1;31msobrepeso\033[m'.format(imc))
elif imc < 40:
    print('Seu imc é de {:.1f}.\n Cuidado! Você está com \033[1;31mObesidade\033[m'.format(imc))
else:
    print('Seu imc é de {:.1f}.\nMuito cudiado! Você está com \033[1;31mObesidade Mórbida\033[m'.format(imc))
