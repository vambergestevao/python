print('\033[1;37m====== DESAFIO 53 ======\033[m')

print('\033[1;33m- Estrutura de Repetição FOR -\033[m')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # Forma uma Lista
junto = ''.join(palavras) # Junta as Palavras
inverso = ''
'''inverso = junto[::-1]''' # Pode ser feito com FATIAMENTO
for letra in range(len(junto) -1, -1, -1): # 1° (-1) - Começa pela última letra, 2° (-1) - Termina na primeira letra e o 3° (-1) - Faz a contagem inversa.
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')
