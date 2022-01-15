velocidade = float(input('Qual a velocadidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você está acima do permitido, 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')
