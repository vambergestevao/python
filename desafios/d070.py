print('\033[1;37m====== DESAFIO 70 ======\033[m')

print('\033[1;33m- Estrutura de Repetição WHILE -\033[m')

print('=' * 18)
print('LOJA SUPER BARATÃO')
print('=' * 18)
total = produtomil = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        produtomil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('=' * 10, end='')
print(' FIM DO PROGRAMA ', end='')
print('=' * 10)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {produtomil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi o(a) {barato} que custa R${menor:.2f}')
