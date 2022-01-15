tot18 = totH = totM20 = 0
while True:
    print('-'*30)
    print('Cadastre uma pessoa')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '  
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total +18: {tot18}')
print(f'Total de Homens Cadastrado: {totH}')
print(f'Total Mulheres -20: {totM20}')