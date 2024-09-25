print('\033[1;37m====== DESAFIO 04 ======\033[m')

print('\033[1;33m- Tipos Primitivos e Saída de Dados -\033[m')

n = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaço? {}'.format(n.isspace()))
print('É um número? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('Está em letras maiúsculas? {}'.format(n.isupper()))
print('Está em letras minúsculas? {}'.format(n.islower()))
print('Está capitalizada? {}'.format(n.istitle()))
