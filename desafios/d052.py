print('\033[1;37m====== DESAFIO 52 ======\033[m')

print('\033[1;33m- Estrutura de Repetição FOR -\033[m')

n = int(input('Digite um número: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi dividido {} vezes'.format(n, t))
if t == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
