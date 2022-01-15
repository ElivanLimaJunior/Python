n1 = float(input('Digite o seu salário. '))
a = 15/100*n1
b = n1+a
print('Você recebeu um aumento de 15% que é equivalente a {:.2f} R$. \nSeu novo salário é de  {:.2f} R$. '.format(a ,b))

# Ou

n2 = float(input('Digite o salário:'))
c = n2 + (15/100*n2)
print('Com o aumento de 15%, o funcionario agora passa a receber {}R$'.format(c))

