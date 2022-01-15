# Esse é o jeito mas facil visto no comentario do youtube
# primeiro vc cria as variaveis...
n1 = int(input('Digite o primeiro numero '))
n2 = int(input('Digite o segundo numero '))
n3 = int(input('Digite o terceiro numero '))
# depois vc cria uma variavel e uma lista para eles
numeros = [n1, n2, n3]
# depois basta printar a lista usando o MAX e o MIN para ele retornar
# o valor maximo e o minimo da lista
print('O menor número digitado é: {}'.format(max(numeros)))
print('O maior número digitado é: {}'.format(min(numeros)))

