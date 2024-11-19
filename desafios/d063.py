print('\033[1;37m====== DESAFIO 63 ======\033[m')

print('\033[1;33m- Estrutura de Repetição WHILE -\033[m')

print('\033[1;36m-\033[m' * 22)
print('\033[1;36mSequência de Fibonacci\033[m')
print('\033[1;36m-\033[m' * 22)

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('\033[1;36m~\033[m' * 40)
print('{} -> {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' -> FIM!')
print('\033[1;36m~\033[m' * 40)
