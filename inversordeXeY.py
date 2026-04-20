print ("informe dois valores para X e Y, respectivamente: ")
x = int(input("valor de X: "))
y = int(input("valor de Y: "))
print ("o valor de X e Y é: ")
print (x, y)
print ("deseja inverter os valores de X e Y? (s/n)")
resposta = input()
if resposta == "s" or resposta == "sim":
    x, y = y, x
    print ("os valores de X e Y foram invertidos: ")
    print (x, y)
if resposta == "n" or resposta == "não":
    print ("os valores de X e Y não foram invertidos: ")
    print (x, y)