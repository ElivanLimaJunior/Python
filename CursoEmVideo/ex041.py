from datetime import date
ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('\nEste é um atleta da categoria MIRIM')
elif idade <= 14:
    print('\nEste é um atleta da categoria INFANTIL')
elif idade <= 19:
    print('\nEste é um atleta da categoria JUNIOR')
else:
    print('\nEste atleta está na categoria MASTER')