''' Escreva um programa que receba um numero e informe quantos divisores ele possui
em divisores exatos o resto da divisão é sempre 0 e o fator sempre e um numero
inteiro.'''

print ('descubra quantos divisores um numero possui')
num = int(input('Digite um numero: '))
contador = 0
for i in range(1, num + 1):
    if num % i == 0:
        contador += 1
print(f'Os divisores de {num} são: ', end='')
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=' ')
print(f'\nO numero {num} possui {contador} divisores exatos')