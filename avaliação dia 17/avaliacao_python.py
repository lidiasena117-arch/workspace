cadastro = int(input("quantos alunos serão cadastrados?"))
turma = []
for i in range(cadastro):
    nome = str(input("qual o nome do aluno?"))
    print(f"Olá, {nome}!")


    N1 = float(input("nota 1:"))
    N2 = float(input("nota 2:"))
    N3 = float(input("nota 3:"))
    media = (N1 + N2 + N3) / 3
    print(f"sua média é: {media:.2f}")


    if media >=7.0:


        print("parabens, você foi aprovado!😃")


    elif media >= 5.0 and media < 7.0:
        print("você está de recuperação, estude 🆗")


    else:
        print("você foi reprovado 😢")
    aluno = [nome, [N1, N2, N3], media]
   
    turma.append(aluno)
for aluno in turma:
 print(f"aluno: {aluno[0]}, notas: {aluno[1][0]}+{aluno[1][1]}+{aluno[1][2]}, média:{aluno[2]:.2f}, situação: {'aprovado' if aluno[2]>=7.0 else 'recuperação' if aluno[2]>=5.0 else 'reprovado'}")
