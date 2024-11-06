print('\033[1;37m====== EXERCÍCIO 11 ======\033[m')

print('\033[1;33m- Estrutura de Repetição WHILE -\033[m')

c = 1
while c < 10:
    print(c)    # Contagem de 1 até 9 (Sempre desconsidera o último)
    c += 1
print('Fim')

n = 1
while n != 0:   # Condição de parada
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar[S/N]? ')).upper()
print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
