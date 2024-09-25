print('\033[1;37m====== DESAFIO 34 ======\033[m')

print('\033[1;33m- Condições e Operadores Aritméticos -\033[m')

sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    nsal = sal + (sal * 15 / 100)
else:
    nsal = sal + (sal * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}!'.format(sal, nsal))
