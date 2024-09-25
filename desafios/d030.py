print('\033[1;37m====== DESAFIO 30 ======\033[m')

print('\033[1;33m- Condições e Operadores Aritméticos -\033[m')

num = int(input('Me diga um número qualquer: '))
res = num % 2
if res == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))
