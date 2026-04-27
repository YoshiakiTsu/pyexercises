while True:
    try:
        numero = float(input("insira o seu número: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números inteiros.")

numero1 = numero * 1
numero2 = numero * 2
numero3 = numero * 3
numero4 = numero * 4
numero5 = numero * 5
numero6 = numero * 6
numero7 = numero * 7
numero8 = numero * 8
numero9 = numero * 9
numero10 = numero * 10

if numero < 0:
    print("o número deve ser positivo")
elif numero == 0:
    print("o número deve ser diferente de zero")
elif numero > 10:
    print("o número deve ser menor ou igual a 10")
else:
    print(f"tabuada do {numero:.0f}")
    print(f"{numero:.0f} x 1 = {numero1:.0f}")
    print(f"{numero:.0f} x 2 = {numero2:.0f}")
    print(f"{numero:.0f} x 3 = {numero3:.0f}")
    print(f"{numero:.0f} x 4 = {numero4:.0f}")
    print(f"{numero:.0f} x 5 = {numero5:.0f}")
    print(f"{numero:.0f} x 6 = {numero6:.0f}")
    print(f"{numero:.0f} x 7 = {numero7:.0f}")
    print(f"{numero:.0f} x 8 = {numero8:.0f}")
    print(f"{numero:.0f} x 9 = {numero9:.0f}")
    print(f"{numero:.0f} x 10 = {numero10:.0f}")