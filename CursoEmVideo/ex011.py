larg = float(input('Qual a largura da parede ?'))
alt = float(input('Qual a altura da parede ?'))
a = larg * alt
print('A dimensão da parede é de {}x{} e sua area é de {}m²'.format(larg, alt, a))
tinta = a / 2
print('para pintar essa parede, você precisa de {}l de tinta'.format(tinta))
