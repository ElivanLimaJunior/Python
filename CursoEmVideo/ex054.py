from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 5):
    n = int(input('Em que a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - n
    if idade >=18:
        totmaior += 1
    else:
        totmenor += 1
print('\n{} de maior.'.format(totmaior))
print('{} de menor.'.format(totmenor))