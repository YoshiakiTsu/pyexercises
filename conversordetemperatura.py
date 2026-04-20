print ("insira a sua temperatura em fahrenheit: ")
temp_f = float(input())
temp_c = (temp_f - 32) * 5.0/9.0
print ("a temperatura em celsius é: ", temp_c)
repeat = input("deseja converter outra temperatura? (s/n) ")
while repeat.lower() == 's':
    print ("insira a sua temperatura em fahrenheit: ")
    temp_f = float(input())
    temp_c = (temp_f - 32) * 5.0/9.0
    print ("a temperatura em celsius é: ", temp_c)
    repeat = input("deseja converter outra temperatura? (s/n) ")
print ("obrigado por usar o conversor de temperatura!")