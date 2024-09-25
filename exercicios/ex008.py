print('\033[1;37m====== EXERCÍCIO 08 ======\033[m')

print('\033[1;36m- Cores no Terminal -\033[m')

a = 33
b = 55
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!'.format(a, b))

nome = 'Python'
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

nome1 = 'Curso'
cores = {'limpar':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;37m'}
print('Olá! Estou fazendo o {}{}{} de Python!'.format(cores['pretoebranco'], nome1, cores['limpar']))
