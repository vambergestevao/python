print('\033[1;37m====== DESAFIO 49 ======\033[m')

print('\033[1;33m- Estrutura de Repetição FOR -\033[m')

num = int(input('Digite um número para ver sua Tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
