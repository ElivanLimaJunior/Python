#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distancia da sua viagem:  '))
print('Você está preste a simular o valor de uma viagem de {:.2f}Km.'.format(distancia))
preço = distancia *0.50 if distancia <=200 else distancia *0.45
print('Sua viagem tera um gasto total de R${:.2f}'.format(preço))

# Essa é uma outra maneira de usar o IF(Se)