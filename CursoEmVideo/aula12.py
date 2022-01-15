nome = str(input('Digite o nome de um membro de sua familia: ')).upper()
if nome == 'ELIVAN JUNIOR':
    print('Seja bem vindo Elivan!')
elif nome == 'ERIC' or nome == 'EVELYN' or nome == 'EVERTON':
    print('Este é um de seus irmão')
elif nome == 'ALEXSANDRA' or nome == 'ELIVAN JOSÉ':
    print('Este é um de seus pais')
elif nome == 'ANTONIO' or nome == 'HELENA' or nome == 'EDGAR':
    print('Este é um de seus avós')
else:
    print('Essa pessoa não faz parte de sua familia')
