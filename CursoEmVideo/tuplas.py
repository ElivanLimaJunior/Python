'''lanche = ('Hambúrguer', 'Suco', 'pizza', 'pudim', 'Batata Frita')'''
#Tuplas são imutáveis
# Não é possível fazer uma alteração nela por ex: "Lanche[3] = 'água'"

'''print('\nManeira 1 de fazer\n')
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')

print('\nManeira 2 de fazer\n')
for comida in lanche:
    print(f'Eu quero {comida}')
print('\nVou sair daqui cheio!!')'''

'''print(sorted(lanche))''' # Sorted Coloca os itens na ordem alfabetica, ele não altera as tuplas, apenas coloca em ordem



# Parte 2
# juntando tuplas. Lembrando que a ordem importa !!! elas vem na ordem que você colocou
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

print('Count\n')
# Vendo quantos números tem em cada tupla.
# com o count é possivel ver quantas vezes determinado número aparece na tupla.
print(c.count(5))
print(c.count(4))
print(c.count(0))

print('\nindex\n')
# Também temos a propriedade index, que retorna na tela em qual posição está determinado valor.
print(c.index(4))
print(c.index(5))
print(c.index(2))
# O Index retorna a primeira ocasião em que o valor aparece.
# Podemos também ver ele a a partir de determinada posição.
# As vezes o mesmo número pode aparecer duas vezes em lugares diferentes, para isso é bom ver a posição.
print('\n Vendo a partir de determinada posição\n')
print(c.index(2)) # Aqui o 5 aparece na posição 1. Este é o primeiro 5 encontrado na tupla, mas podemos ver q tem outro 5 present.
print('\nLocalizando o segundo valor presente\n')
print(c.index(2, 1))

# as tuplas são imutaveis, + é possivel apagar ela. Porém só é possivel apagar apenas por completo!
'''del(a)''' # dessa maneira a tupla será excluida por completo.