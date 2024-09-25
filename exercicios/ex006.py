print('\033[1;37m====== EXERCÍCIO 06 ======\033[m')

print('\033[1;33m- Cadeias de Texto -\033[m')

frase = 'Curso em Vídeo Python'

print('\033[0;33m- Fatiamento\033[m:')
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(frase[9:21:2])

print('\033[0;33m- Análise\033[m:')
print(len(frase))
print(frase.count('o',0,13))
print(frase.count('o'))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

print('\033[0;33m- Transformação\033[m:')
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

print('\033[0;33m- Divisão\033[m:')
print(frase.split())

print('\033[0;33m- Junção\033[m:')
# print('-'.join(frase))
print(frase.split('-'.join(frase)))

# Uma string, em seus microselementos, é imutável.
# Para marcar todo um texto na linguagem Python basta usar (""") no início e no final.
