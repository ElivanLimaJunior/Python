salario = int(input('Qual o seu salario atual ? '))
s10 = (salario*0.10) + salario
s15 = (salario*0.15) + salario
if salario > 1250:
    print('Com um aumento de 10% seu salario fica : R${:.2f} '.format(s10))
else:
    print('Com um aumento de 15% seu salario fica : R${:.2f} '.format(s15))