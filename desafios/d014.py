print('====== DESAFIO 14 ======')

tempc = float(input('Informe a temperatura em °C: '))

# tempf = ((9 * tempc) / 5) + 32
# tempf = (tempc * 1,8) + 32
tempf = (tempc * 9/5) + 32

print('A temperatura de {}°C corresponde a {}°F!'.format(tempc, tempf))
 