print('====== DESAFIO 12 ======')

val = float(input('Qual é o preço do produto? R$ '))

pd = val - (val * 5 / 100)
# pd = val - (val * 0.05)

print('O produto que custa R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(val, pd))
