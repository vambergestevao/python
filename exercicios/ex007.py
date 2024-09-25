print('\033[1;37m====== EXERCÍCIO 07 ======\033[m')

print('\033[1;33m- Condições (Simples, Compostas, Simplificadas) -\033[m')

# Condições Simples
nome = str(input('Digite seu nome: ')).strip().title()
if nome == 'Maria':
    print('Seu nome é lindo!')
print('Prazer em te conhecer, {}!'.format(nome))
print('\033[0;33m--- Fim ---\033[m')

# Condições Compostas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Seu média foi boa, PARABÊNS!')
else:
    print('Sua média foi ruim, ESTUDE MAIS!')

# Condições Simplificadas
print('PARABÊNS!' if m >= 6 else 'ESTUDE MAIS!')
