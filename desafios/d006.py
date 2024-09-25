print('\033[1;37m====== DESAFIO 06 ======\033[m')

print('\033[1;33m- Operadores Aritméticos -\033[m')

n = int(input('Digite um número: '))

# d = n * 2
# t = n * 3
# r = n ** (1/2)

# print('O dobro de {} vale {}'.format(n, d))
# print('O triplo de {} vale {}'.format(n, t))
# print('A raiz quadrada de {} é igual a {:.2f}'.format(n, r))

# A função 'pow(n, (1/2))', calcula a raiz quadrada.  

print('O dobro de {} vale {}'.format(n, (n*2)))
print('O triplo de {} vale {}'.format(n, (n*3)))
print('A raiz quadrada de {} é igual a {:.2f}'.format(n, (n**(1/2))))
