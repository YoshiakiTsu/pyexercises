print ('descubra qual o fatorial do seu numero')
n = int(input('digite um numero: '))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f'O fatorial de {n} é {fatorial}')