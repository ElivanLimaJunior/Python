nome = str(input('Digite o nome do aluno. '))
n1 = float(input('Digite a nota de Português. '))
n2 = float(input('Digite a nota de matématica. '))
n3 = float(input('Digite a nota de ciências. '))
n4 = float(input('Digite a nota de Historia '))
n5 = float(input('Digite a nota de Geografia '))
m = (n1 + n2 + n3 + n4 + n5) / 5
print('A média do(a) aluno {} esse ano foi {} '.format(nome,m))

if m>20:
    print('\n \nCongratulations')
else:
    print('\n \nGame Over')