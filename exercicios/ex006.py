print('====== EXERCÍCIO 06 ======')

frase = 'Curso em Vídeo Python'

print('- Fatiamento:')
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(frase[9:21:2])

print('- Análise:')
print(len(frase))
print(frase.count('o',0,13))
print(frase.count('o'))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

print('- Transformação:')
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

print('- Divisão:')
print(frase.split())

print('- Junção:')
# print('-'.join(frase))
print(frase.split('-'.join(frase)))

# Uma string, em seus microselementos, ela é imutável.

# Para marcar todo um texto na linguagem Python basta usar (""") no início e no final.
