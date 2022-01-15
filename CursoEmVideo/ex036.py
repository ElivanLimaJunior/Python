casa = float(input('Qual o valor da Casa? '))
salario = float(input('Qual o seu salario mensal? '))
parcelas = int(input('Em quantos anos você pretende pagar? '))
qtparcelas = parcelas * 12
n1 = salario*30/100
n2 = casa/ (parcelas * 12)
print("Para pagar uma casa no valor de {:.2f} R$ em {} anos a prestação será de {:.2f} R$".format(casa, parcelas, n2))
if n1 >= n2:
    print('Parabéns!!! \n Empréstimo APROVADO!\nVocê irá pagar {:.2f} R$ parcelas de {:.2f} R$'.format(qtparcelas, n1))
else:
    print('Desculpe... \n Seu emprestimo foi NEGADO!')