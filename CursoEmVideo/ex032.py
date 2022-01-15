# Programa para ler se o a no é BISSEXTO ou não.
# 1 importar a biblioteca datetime, escolher apenas a função date que é a que  será usada
from datetime import date
ano = int(input('Que ano quer analisar? '))
# usar a formula IF(SE) para analisar se o ano digitado for 0, será igual a date.today().year.
# date.today() irá pegar a data de hoje e o .year irá trazer o que eu quero da data de hoje que no caso é o ano
# então se o usuario digitar 0 o programa irá trazer o ano de hoje automaticamente.
if ano == 0:
    ano = date.today().year
# aqui é usado o se(IF) com o and para fazer um outro se(IF) dentro dele. analisar duas situações diferentes.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
