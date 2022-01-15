sexo = int(input('''Informe seu sexo:
[ 1 ] Masculino: 
[ 2 ] Feminino: '''))

if sexo == 1:
    data = int(input('Digite o ano em que nasceu: '))
    prazo = 2021 - data
    tempo = 18 - prazo
    passou = prazo - 18
    idade = data + 18
    if prazo == 18:
        print('Vejo que você tem {} anos, \n\033[1;32mEste é o ano de seu alistamento.\033[m'.format(prazo))
    elif prazo < 18:
        print('Vejo que você tem {} anos, ainda não está na hora de se alistar. \n\033[1;34mVolte daqui a {} anos.\033[m\nMas precisamente em {}.'.format(prazo, tempo, idade))
    elif prazo > 18:
        print('Você já está com {} anos, \n\033[1;33mNote que já passou {} anos do prazo para se alistar\033[m\nSeu alistamento foi em {}'.format(prazo, passou, idade))
elif sexo == 2:
    print('\n\n\033[1;36mO alistamento Feminino não é obrigatorio\033[m')