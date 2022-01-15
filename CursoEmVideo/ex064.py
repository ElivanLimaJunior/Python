n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
print('Você usou {} Números e a soma deles é {}.'.format(cont -1, soma - 999))
print('FIM')

# outra maneira legal

n1 = cont = soma = 0
n1 = int(input('Digite um número: '))
while n1 != 999:
    soma += n1
    cont += 1
    n1 = int(input('Digite um número: '))
print('Você usou {} Números e a soma deles é {}.'.format(cont, soma))
print('FIM')

'''Do Jeito 2, Definindo a Variavel do lado de fora irá fazer com que
Após eu Digitar 999 ele quebre o FLAG  antes de entrar no While 
            Pois a Condição já sera Verdadeira.'''