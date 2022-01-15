'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
caso esteja errado, peça a digitação novamente até ter um valor correto.'''

s = 0
r = '\nOpção inválida! Digite novamente por favor\n'
while s != 'M' and s != 'F':
    s = str(input('Por favor informe seu sexo: [F/M]: ')).upper().strip()[0] # as [] com o zero no meio é um fatiamento de string. irá pegar apenas a primeira letra.
    if s == 'F':
         print('\n\033[32mFeminino')
    elif s == 'M':
        print('\n\033[32mMasculino')
    else:
        print('{}'.format(r))
print('\n\033[mFim')


# Jeito Guanabara

'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip.upper()[0]
print('Sexo {} registrado com Sucesso!!'.format(sexo))'''
