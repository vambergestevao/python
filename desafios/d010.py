print('\033[1;37m====== DESAFIO 10 ======\033[m')

print('\033[1;33m- Operadores Aritméticos -\033[m')

n = float(input('Quanto você tem na carteira? R$ '))

# d = n / 5.44

print('Com R${:.2f} você pode comprar US$ {:.2f}'.format(n, (n/5.44)))
