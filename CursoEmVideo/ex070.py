print('~~'*20)
print('            Loja Super Baratão        ')
print('~~'*20)
op = valor = mil = preço = 0
min = 9999999
barato = ' '
while True:
    item = str(input('Nome do produto: '))
    preço = int(input('Preço: R$'))
    op = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    valor += preço
    if preço >= 1000:
       mil += 1
    elif preço <= min:
        min = preço
        barato = item
    if op == 'N':
        break
print(f'\nO valor todal de suas compras é de R$ {valor}')
print(f'\nO produto mas barato da lista foi {barato} que custou R$ {min}')
print(f'\nVocê tem {mil} compras acima de R$ 1000')
print('Fim')
