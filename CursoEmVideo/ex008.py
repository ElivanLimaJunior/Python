n1 = float(input('Digite um valor para convertelo '))
a = n1/1000
b = n1/100
c = n1/10
d = n1*10
f = n1*100
g = n1*1000
print('{} metros corresponde a:\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm '.format(n1, a, b, c, d, f, g))
