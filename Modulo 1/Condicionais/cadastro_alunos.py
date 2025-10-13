nome = []

idade = []

categoria = []

while True:

    print("Escolha a opção abaixo: ")

    print("opção 1 - Cadastrar alunos")

    print("opção 2 - Exibir alunos")

    print("opção 3 - Fechar Progama")

    opcao = int(input("Insira aqui sua opção: "))

    if opcao == 1:

        nome1 = input("Digite o nome do aluno: ")

        categoria1 = input("Digite a categoria entre A, B, AB: ")

        idade1 = int(input("Digite a idade do aluno: "))

        if idade1 < 18:

            print("Impossivel realizar o cadastro, aludo de menor idade")

        elif categoria1 not in ['a','b','ab','A','B','AB']:

            print("Categoria invalida, tente novamente")

        else :

            nome.append(nome1)

            idade.append(idade1)

            categoria.append(categoria1)

            print("Cadastro realizado com sucesso")

            sim_não = input("Deseja realizar mais um cadastro? S(sim) N(não): ")

            if sim_não in ['s','n','S','N']:
                
                print("Prossiga")
            else: 

                print("Opção invalida, tente novamente")

    elif opcao == 2:

        for nome, idade, categoria in zip(nome, idade, categoria):

            print("| NOME | IDADE | CATEGORIA |")

            print(f"{nome} {idade} {categoria} ")

    elif opcao == 3:

        print("Encerrando o Progama")
        
        break