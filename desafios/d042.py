print('\033[1;37m====== DESAFIO 42 ======\033[m')

print('\033[1;33m- Condições Aninhadas -\033[m')

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um Triângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO!')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um Triângulo!')
