print('\033[1;37m====== DESAFIO 44 ======\033[m')

print('\033[1;33m- Condições Aninhadas -\033[m')

print('\033[1;34m=-=-= LOJAS ESTEVÃO =-=-=\033[m')

valor = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista Dinheiro/Cheque
[ 2 ] à vista Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    desc = valor - (valor * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, desc))
elif op == 2:
    desc = valor - (valor * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, desc))
elif op == 3:
    parcela = valor / 2
    total = parcela * 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))
elif op == 4:
    juros = valor + (valor * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = juros / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, juros))
else:
    total = valor
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente!')
