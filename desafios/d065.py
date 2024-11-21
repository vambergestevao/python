print('\033[1;37m====== DESAFIO 65 ======\033[m')

print('\033[1;33m- Estrutura de Repetição WHILE -\033[m')

r = 'S'
quant = soma = média = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    quant += 1
    soma += n
    if quant == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {:.2f}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
