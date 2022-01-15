'''leia(n1,n2)
se ((n1 < 2) e (n2 < 5 )) entao
      escreva("O valor foi: ", n1)
senao
       se ((n1 > 1) e (n2 > 4) ) entao
            escreva ("O valor foi: ", n1+2 )
       senao
            se ((n1 > 3) ou (n2 < 10)) entao
                   escreva("O valor foi: ", n2+n1)
            senao
                  escreva("O valor foi: ", 5)'''

n1 = 2
n2 = 4
if n1 < 2 and n2 < 5:
    print('O valor foi: {}'.format(n1))
else:
    if n1 > 1 and n2 > 4:
        print('O valor foi: {}'.format(n1+2))
    else:
        if n1 > 3 and n2 < 10:
            print('O valor foi: {}'.format(n2+n1))
        else:
            print('O valor foi: {}'.format(5))
print('Fim')