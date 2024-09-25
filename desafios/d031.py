print('\033[1;37m====== DESAFIO 31 ======\033[m')

print('\033[1;33m- Condições e Operadores Aritméticos -\033[m')

dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(dist))
# if dist <= 200:
#     preço = 0.50 * dist
# else:
#     preço = 0.45 * dist
preço = dist * 0.50 if dist <= 200 else dist * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
