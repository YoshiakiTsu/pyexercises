print ('descubra se a area do quadrado é maior ou menor que a área do triangulo')
lado = float(input('insira o lado do quadrado: '))
area_quadrado = lado * lado
print('a área do quadrado é: ', area_quadrado)

base = float(input('insira a base do triangulo: '))
altura = float(input('insira a altura do trinagulo: '))
area_triangulo = base * altura / 2
print('a área do triangulo é: ', area_triangulo)

if area_triangulo > area_quadrado:
    print('a área do triangulo é maior do que a área do quadrado')
else:
    print('a área do quadrado é maior que a área do triangulo')