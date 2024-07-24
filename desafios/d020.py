print('====== DESAFIO 20 ======')

# import random
# a1 = str(input('Primeiro aluno: '))
# a2 = str(input('Segundo aluno: '))
# a3 = str(input('Terceiro aluno: '))
# a4 = str(input('Quarto aluno: '))
# lista = [a1, a2, a3 ,a4]
# ordem = random.shuffle(lista)
# print('A ordem de apresentação será ')
# print(lista)


from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3 ,a4]
ordem = shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
