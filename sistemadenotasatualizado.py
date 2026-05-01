print ("sistema de cálculo de média dos alunos")
nome_aluno = input("insira o nome do Aluno: ")
while True:
    try:
        nota1 = float(input("insira a primeira nota: "))
        nota2 = float(input("insira a segunda nota: "))
        nota3 = float(input("insira a terceira nota: "))
        nota4 = float(input("insira a quarta nota: "))
    except Exception as e :
        print(f'Erro insira um valor valido ,{e} ')
    
    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 7:
        print ("o aluno", nome_aluno, "teve a média", f"{media:.2f}", "e foi aprovado")
    elif media <= 3:
        print ("o aluno", nome_aluno, "teve a média", f"{media:.2f}", "e foi reprovado")
    else:
        print ("o aluno", nome_aluno, "teve a média", f"{media:.2f}", "e está de recuperação")
