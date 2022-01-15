#Crie uma tupla preenchuda com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# A) Apenas os 5 primeiros colocados
# B) os 4 últimos colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da chapecoense

times= ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Atlético-GO', 'Ceará SC', 'Athletico-PR', 'Internacional', 'Santos', 'São Paulo', 'Juvetude', 'Cuiabá', 'Bahia', 'Fluminense', 'Grêmio', 'Sport Recife', 'América-MG', 'Chapecoense')
print(f'Os cinco primeiros colocados:\n{times[0:5]}')
print(f'\nOs 4 últimos colocados da tabela:\n{times[16:20]}')
print(f'\nLista dos times em ordem alfabética:\n{sorted(times[0:])}')
Chapecoense = times.index('Chapecoense') + 1
print(f'\nO Chapecoense está na {Chapecoense}ª posição')

