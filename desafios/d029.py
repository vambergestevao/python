print('\033[1;37m====== DESAFIO 29 ======\033[m')

print('\033[1;33m- Condições e Operadores Aritméticos -\033[m')

# vel = float(input('Qual é a velocidade atual do carro? '))
# m = 7 * (vel - 80)
# if vel <= 80:
#     print('Tenha um bom dia! Dirija com segurança!')
# else:
#     print('MULTADO! Você excedeu o limite permitido que é de 80Km/h!')
#     print('Você deve pagar uma multa de R${:.2f}!'.format(m))
#     print('Tenha um bom dia! Dirija com segurança!')

vel = float(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h!')
    m = 7 * (vel - 80)
    print('Você deve pagar uma multa de R${:.2f}!'.format(m))
print('Tenha um bom dia! Dirija com segurança!')
