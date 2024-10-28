print('\033[1;37m====== DESAFIO 51 ======\033[m')

print('\033[1;33m- Estrutura de Repetição FOR -\033[m')

print('\033[1;36m=\033[m' * 20)
print('\033[1;36m10 TERMOS DE UMA PA\033[m')
print('\033[1;36m=\033[m' * 20)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r # enésimo termo de uma pa
for c in range(p, d+r, r):
    print(c, end=' -> ')
print('ACABOU')
