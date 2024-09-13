print('====== DESAFIO 17 ======')

# from math import sqrt
# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# co = co * co
# ca = ca * ca
# hi = sqrt(co+ca)
# print('A hipotenusa vai medir {:.2f}'.format(hi))

# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hi))

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
