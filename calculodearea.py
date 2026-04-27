print("calculadora de área de formas geométricas")
print("1. Quadrado")
print("2. Triângulo")
print("3. Trapézio")
print("insira as medidas de cada uma das formas geométricas e descubra qual tem a maior área")
input("aperte enter para começar")
print("insira as medidas do quadrado")
lado = float(input("lado: "))
area_quadrado = lado * lado
print("área do quadrado: ", area_quadrado)
print("insira as medidas do triângulo")
base = float(input("base: "))
altura = float(input("altura: "))
area_triangulo = (base * altura) / 2
print("área do triângulo: ", area_triangulo)
print("insira as medidas do trapézio")
base_maior = float(input("base maior:" ))
base_menor = float(input("base menor: "))
altura_trapezio = float(input("altura: "))
area_trapezio = ((base_maior + base_menor) * altura_trapezio) / 2
print("área do trapézio: ", area_trapezio)
if area_quadrado > area_triangulo and area_quadrado > area_trapezio:
    print("o quadrado tem a maior área")
elif area_triangulo > area_quadrado and area_triangulo > area_trapezio:
    print("o triângulo tem a maior área")
elif area_trapezio > area_quadrado and area_trapezio > area_triangulo:
    print("o trapézio tem a maior área")
else:    print("as áreas são iguais")  