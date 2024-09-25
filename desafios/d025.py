print('\033[1;37m====== DESAFIO 25 ======\033[m')

print('\033[1;33m- Cadeias de Texto -\033[m')

# nome = str(input('Qual é o seu nome completo? ')).strip().title()
# print('Seu nome tem Silva? {}'.format('Silva' in nome))

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.title()))
