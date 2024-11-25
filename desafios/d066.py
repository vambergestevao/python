print('\033[1;37m====== DESAFIO 66 ======\033[m')

print('\033[1;33m- Estrutura de Repetição WHILE -\033[m')

s = v = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    v += 1
    s += n
print(f'A soma dos {v} valores foi {s}!')
