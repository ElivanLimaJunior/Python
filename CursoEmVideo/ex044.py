print('{:~^40}'.format('Bem vindo a Loja do Elivan'))
p1= float(input("Qual o valor do produto ? "))
opção = int(input('''Selecione o meio de pagamento
[ 1 ] Dinheiro ou Cheque. 
[ 2 ] Cartão. 
[ 3 ] 2x Sem Jurus. 
[ 4 ] Em 3x ou mais.\n  '''))
if opção == 1:
    total = p1 - (p1 * 10 / 100)
    print('Pagamentos a vista tem 10% de desconto, você irá pagar R${}.'.format(total))
elif opção == 2:
    total = p1 - (p1 * 5 / 100)
    print('Pagamentos no cartão tem 5% de desconto, você irá pagar R${}.'.format(total))
elif opção == 3:
    total = p1
    parcela = total / 2
    print('Sua compra de R${} será parcelada em 2x R${} sem descontos inclusos.'.format(p1, parcela))
elif opção == 4:
    qt = int(input('Em quantas vezes você quer parcelar ? '))
    total = p1 + (p1 * 25 / 100)
    jurus = total / qt
    print('Parcelando em {}x o valor pago será R${} com um jurus de 25%.'.format(qt, jurus))
else:
    print('Opção incorreta, escolha uma opção valida por favor.')
print('Sua compra de R${} vai está custando R${}.'.format(p1, total))