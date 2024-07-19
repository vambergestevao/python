print('====== DESAFIO 18 ======')

# import math
# an = float(input('Digite o ângulo que você deseja: '))
# s = math.sin(math.radians(an))
# c = math.cos(math.radians(an))
# t = math.tan(math.radians(an))
# print('O ângulo de {} tem o SENO de {:.2f}'.format(an, s))
# print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, c))
# print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, t))


from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(an))
c = cos(radians(an))
t = tan(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, s))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, c))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, t))
