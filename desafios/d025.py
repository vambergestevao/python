print('====== DESAFIO 25 ======')

# nome = str(input('Qual é o seu nome completo? ')).strip().title()
# print('Seu nome tem Silva? {}'.format('Silva' in nome))

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.title()))
