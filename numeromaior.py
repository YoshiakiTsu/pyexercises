print ("revelando o número maior")
num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))
num3 = float(input("digite o terceiro número: "))
if num1 > num2 and num1 > num3:
    print("o número maior é: ", num1)
elif num2 > num1 and num2 > num3:
    print("o número maior é: ", num2)
else:    print("o número maior é: ", num3)