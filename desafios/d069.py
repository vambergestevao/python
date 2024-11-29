print('\033[1;37m====== DESAFIO 69 ======\033[m')

print('\033[1;33m- Estrutura de Repetição WHILE -\033[m')

print('=' * 20)
print('CADASTRE UMA PESSOA')
print('=' * 20)
sexo = total = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('~' * 25)
    if idade >= 18:
        total += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres +=  1
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
    print('~' * 25)
print(f'Total de pessoas com mais de 18 anos: {total}')
print(f'Ao todo temos {homens} homens cadrastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
