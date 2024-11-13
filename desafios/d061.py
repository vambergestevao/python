print('\033[1;37m====== DESAFIO 61 ======\033[m')

print('\033[1;33m- Estrutura de Repetição WHILE -\033[m')

print('\033[1;32m=\033[m' * 14)
print('\033[1;32mGERADOR DE PA\033[m')
print('\033[1;32m=\033[m' * 14)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = p
c = 1
while c <= 10:
    print('{} -> '.format(t), end='')
    t += r
    c += 1
print('Fim')
