print('====== DESAFIO 35 ======')

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    tri = 'PODEM FORMAR'
else:
    tri = 'NÃO PODEM FORMAR'
print('Os segmentos acima {} um Triângulo!'.format(tri))
