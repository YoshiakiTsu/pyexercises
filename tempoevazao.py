print ("calcule o volume e o tempo gasto para encher a sua piscina")
comprimento = float(input("digite o comprimento da piscina: "))
largura = float(input("insira a largura da piscina: "))
profundidade = float(input("insira a profundidade da piscina: "))
vazao = 20  # vazão da bomba em metros cúbicos por minuto
volume = comprimento * largura * profundidade
tempo = volume/vazao
print ("o volume da piscina é de: ", volume, "metros cúbicos")
print ("o tempo gasto pra encher a piscina é de ", tempo, "minutos")
