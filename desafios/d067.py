print('\033[1;37m====== DESAFIO 67 ======\033[m')

print('\033[1;33m- Estrutura de Repetição WHILE -\033[m')

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
