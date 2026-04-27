print ("sistema de cálculo de média dos alunos")
nome_aluno = input("insira o nome do Aluno: ")
nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))
nota3 = float(input("insira a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 6:
    print ("o aluno", nome_aluno, "teve a média", f"{media:.2f}", "e foi aprovado")
elif media <= 2:
    print ("o aluno", nome_aluno, "teve a média", f"{media:.2f}", "e foi reprovado")
else:
    print ("o aluno", nome_aluno, "teve a média", f"{media:.2f}", "e está de recuperação")