print('====== EXERCÍCIO 04 ======')

# import math
# n = int(input('Digite um número: '))
# raiz = math.sqrt(n)
# print('A raiz de {} é igual a {:.2f}'.format(n, raiz))


from math import sqrt, floor
n = int(input('Digite um número: '))
raiz = sqrt(n)
print('A raiz de {} é igual a {:.2f}'.format(n, floor(raiz)))
