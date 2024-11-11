print('\033[1;37m====== DESAFIO 59 ======\033[m')

print('\033[1;33m- Estrutura de Repetição WHILE -\033[m')

from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
op = 0
maiornum = 0
while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos valores
    [ 5 ] sair do programa''')
    op = int(input('>>>>> Qual é a sua opção? '))
    if op == 1:
        soma = num1 + num2
        print('A soma entre {} + {} é {}'.format(num1, num2, soma))
    elif op == 2:
        mult = num1 * num2
        print('A multiplicação entre {} x {} é {}'.format(num1, num2, mult))
    elif op == 3:
        # if num1 > num2:
        #     maior = num1
        # else:
        #     maior = num2
        maiornum += 1
        maiornum = num1 and num2
        if num1 > maiornum:
            maiornum = num1
        if num2 > maiornum:
            maiornum = num2
        print('O maior valor entre {} e {}, é {}'.format(num1, num2, maiornum))
    elif op == 4:
        print('Informe novos valores:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('-=' * 15)
    sleep(2)
print('Fim do programa, volte sempre!')
