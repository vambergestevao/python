print('====== DESAFIO 11 ======')

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

# Sabendo que cada litro de tinta, pinta um área de 2m².

ar = larg * alt
lit = ar / 2
# lit = ar * (1/2)

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, ar))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(lit))
