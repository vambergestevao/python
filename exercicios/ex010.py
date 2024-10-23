print('\033[1;37m====== EXERCÍCIO 10 ======\033[m')

print('\033[1;33m- Estrutura de Repetição FOR -\033[m')

for c in range(0, 6):
    print('Oi')
print('Fim!')

print('\033[1;31m=-\033[m' * 15)

for c in range(0, 6): # Sempre desconsidera o último número
    print(c)
print('Fim!')

print('\033[1;31m=-\033[m' * 15)

for c in range(6, 0, -1): # (-1) Contagem Regressiva
    print(c)
print('Fim!')

print('\033[1;31m=-\033[m' * 15)

for c in range(0, 7, 2): # (2) Conta de 2 em 2
    print(c)
print('Fim!')

print('\033[1;31m=-\033[m' * 15)

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim!')

print('\033[1;31m=-\033[m' * 15)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim!')

print('\033[1;31m=-\033[m' * 15)

for c in range(0, 4):
    n = int(input('Digite um valor: '))
print('Fim!')

print('\033[1;31m=-\033[m' * 15)

s = 0 # Acumulador
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n # s = s + n (Acumulador)
print('O somatório de todos os valores foi {}'.format(s))
