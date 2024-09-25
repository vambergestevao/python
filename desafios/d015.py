print('\033[1;37m====== DESAFIO 15 ======\033[m')

print('\033[1;33m- Operadores Aritméticos -\033[m')

# custo do veiculo = R$60 pelo dia
# custo por km = R$0.15 por km rodado

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

# d = d * 60
# km = km * 0.15
# t = d + km

t = (d * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(t))
