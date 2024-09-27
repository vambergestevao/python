print('\033[1;37m====== EXERCÍCIO 09 ======\033[m')

print('\033[1;33m- Condições Aninhadas -\033[m')

nome = str(input('Qual é o seu nome? '))
if nome == 'Maria':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Carla' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana, Cláudia, Jéssica, Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é comum.')
print('Tenha um bom dia, {}!'.format(nome))
