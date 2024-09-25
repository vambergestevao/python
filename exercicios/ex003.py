print('\033[1;37m====== EXERCÍCIO 03 ======\033[m')

print('\033[1;33m- Operadores Aritméticos -\033[m')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto {} \n e a divisão é {:.2f}'.format(s, m, d), end=', portanto a ')
print('divisão inteira é {} e a potência {}'.format(di, e))

# \n -> quebra a linha.
# end= -> junta com o 'print' seguinte.
