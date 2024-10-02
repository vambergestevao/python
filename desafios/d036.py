print('\033[1;37m====== DESAFIO 36 ======\033[m')

print('\033[1;33m- Condições Aninhadas -\033[m')

casa = float(input('Valor da casa? R$'))
sal = float(input('Salário do comprador? R$'))
anos = float(input('Quantos anos de financiamento? '))
prest = casa / (anos * 12)
min = sal * 30 /100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prest))
if prest <= min:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
