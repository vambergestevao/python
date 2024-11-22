print('\033[1;37m====== EXERCÍCIO 12 ======\033[m')

print('\033[1;33m- Interrompendo Repetições WHILE -\033[m')

n = s = v = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break   # Condição de parada
    v += 1
    s += n
print(f'A soma dos {v} valores foi {s}!')   # f-strings (PYTHON 3 - 3.6+)
# print('A soma vale {}'.format(s)) (PYTHON 3)

nome = 'José'
idade = 33
salário = 987.3
print(f'0 {nome} tem {idade} anos e ganha R$ {salário:.2f}')
