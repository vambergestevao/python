print('\033[1;37m====== DESAFIO 07 ======\033[m')

print('\033[1;33m- Operadores Aritméticos -\033[m')

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

# m = (n1+n2) / 2

print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, (n1+n2)/2))
