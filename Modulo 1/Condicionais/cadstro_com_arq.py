
while True:

    print("| Escolha uma opção")
    print("| opção 1 - Adicionar um cadastro")
    print("| opção 2 - Exibir cadastros")
    print("| opção 3 - Encerrar o sistema")


    opcao = int(input())

    if opcao == 1 :

        nome = input("| Digite o nome do aluno: ")

        email = input("| Digite o email: ")

        with open("pessoa.txt", "a") as arquivo:
            arquivo.write("| Nome: " + nome + " | " + "Email: " + email + "\n")

        print("| Cadastro Realizado com sucesso")

    elif opcao == 2:

        try:

            with open("pessoa.txt", "r") as arquivo:
                conteudo = arquivo.read()
                print(conteudo)

        except:

            nome = input("| Digite o nome do aluno: ")

            email = input("| Digite o email: ")

            with open("pessoa.txt", "a") as arquivo:
                arquivo.write("| Nome: " + nome + " | " + "Email: " + email + "\n")

            print("| Cadastro Realizado com sucesso")


    elif opcao == 3:
    
        print("| encerrando sistema")
        break

    else: 
        print("| opção inválida")
