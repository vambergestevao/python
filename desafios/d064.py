print('\033[1;37m====== DESAFIO 64 ======\033[m')

print('\033[1;33m- Estrutura de Repetição WHILE -\033[m')

n = c = s = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(c, s))
