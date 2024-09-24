print('====== DESAFIO 34 ======')

sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    nsal = sal + (sal * 15 / 100)
else:
    nsal = sal + (sal * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(sal, nsal))
