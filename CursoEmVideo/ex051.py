i = int(input('Primeiro termo: '))
r = int(input('razão: '))
d = i + (10 - 1) * r # Essa formula matématica serve para trazer o decimo numero. pode ser alterado
for c in range(i, d + r, r): # Decimo + Razão para ele concluir os 10 numeros
    print(c)