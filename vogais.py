print ("irei descobrir o numero de vogais presente em cada palavra")
palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
contador = 0
for letra in palavra:
    if letra in vogais:
        contador += 1
print(f"A palavra '{palavra}' tem {contador} vogais.")