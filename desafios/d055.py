print('\033[1;37m====== DESAFIO 54 ======\033[m')

print('\033[1;33m- Estrutura de Repetição FOR -\033[m')

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR peso lido foi de {}Kg'.format(maior))
print('O MENOR peso lido foi de {}Kg'.format(menor))
