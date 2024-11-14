print('\033[1;37m====== DESAFIO 62 ======\033[m')

print('\033[1;33m- Estrutura de Repetição WHILE -\033[m')

print('\033[1;30m=\033[m' * 14)
print('\033[1;30mGERADOR DE PA\033[m')
print('\033[1;30m=\033[m' * 14)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
total = 0
maistermos = 10
quantidadetermos = 0
while maistermos != 0:
    total += maistermos
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        c += 1
    print('PAUSA')
    maistermos = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
