print('\033[1;37m====== DESAFIO 40 ======\033[m')

print('\033[1;33m- Condições Aninhadas -\033[m')

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
m = (nota1 + nota2) / 2
if m >= 7.0:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, m))
    print('O aluno está APROVADO.')
elif m >= 5.0 and m <= 6.9:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, m))
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, m))
    print('O aluno está REPROVADO.')

# if 7 > m >= 5:
#     print('RECUPERAÇÃO')
# elif m < 5:
#     print('REPROVADO')
# elif m >= 7:
#     print('APROVADO')
