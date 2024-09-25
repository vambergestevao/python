print('\033[1;37m====== DESAFIO 26 ======\033[m')

print('\033[1;33m- Cadeias de Texto e Operadores Aritméticos -\033[m')

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))
