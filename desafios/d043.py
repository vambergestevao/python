print('\033[1;37m====== DESAFIO 43 ======\033[m')

print('\033[1;33m- Condições Aninhadas -\033[m')

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (M) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 < imc < 25:
    print('Você está na faixa de PESO IDEAL, PARABÉNS!')
elif 25 < imc < 30:
    print('Você está na faixa de SOBREPESO!')
elif 30 < imc < 40:
    print('Você está na faixa de OBESIDADE!')
else:
    print('Você está na faixa de OBESIDADE MÓRBIDA, CUIDADO!')
