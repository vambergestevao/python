print('\033[1;37m====== DESAFIO 48 ======\033[m')

print('\033[1;33m- Estrutura de Repetição FOR -\033[m')

soma = 0 # Acumulador
cont = 0 # Contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c # soma = soma + c - (Pega todos os valores que são "DIVISÍVEIS POR 3" e "SOMA")
        cont += 1 # cont = cont + 1 - (Conta todos os valores que são "DIVISÍVEIS POR 3")
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
