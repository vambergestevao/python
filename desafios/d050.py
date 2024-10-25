print('\033[1;37m====== DESAFIO 50 ======\033[m')

print('\033[1;33m- Estrutura de Repetição FOR -\033[m')

soma = 0 # Acumulador
cont = 0 # Contgador
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num # Pega todos os valores que são "DIVISÍVEIS POR 2" e "SOMA"
        cont += 1 # Conta todos os valores que são "DIVISÍVEIS POR 2"
print('Você informou {} valores PARES e a SOMA foi {}'.format(cont, soma))
