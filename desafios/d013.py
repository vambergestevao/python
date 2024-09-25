print('\033[1;37m====== DESAFIO 13 ======\033[m')

print('\033[1;33m- Operadores Aritméticos -\033[m')

sal = float(input('Qual é o salário do funcionário? R$ '))

aum = sal + (sal * 15 / 100)
# aum = sal + (sal * 0.15)

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(sal, aum))
