print('\033[1;37m====== DESAFIO 38 ======\033[m')

print('\033[1;33m- Condições Aninhadas -\033[m')

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O PRIMEIRO valor é maior!')
elif num2 > num1:
    print('O SEGUNDO valor é maior!')
else:
    print('Os dois valores são IGUAIS!')
