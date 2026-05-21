alunos = []


def cadastrar_aluno():
    print("\n--- Cadastro de Aluno ---")

    nome = input("Digite o nome do aluno: ").strip()

    if nome == "":
        print("Nome inválido!")
        return

    alunos.append(nome)
    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    print("\n--- Lista de Alunos ---")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    cont = 1
    for aluno in alunos:
        print(f"{cont} - {aluno}")
        cont += 1


def update():
    print("\n--- Atualizar Aluno ---")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    listar_alunos()

    try:
        posicao = int(input("Digite a posição do aluno que deseja atualizar: "))
    except ValueError:
        print("Digite um número válido!")
        return

    if posicao < 1 or posicao > len(alunos):
        print("Posição inválida!")
        return

    novo_nome = input("Digite o novo nome do aluno: ").strip()

    if novo_nome == "":
        print("Nome inválido!")
        return

    alunos[posicao - 1] = novo_nome
    print("Aluno atualizado com sucesso!")


def delete():
    print("\n--- Excluir Aluno ---")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    listar_alunos()

    try:
        posicao = int(input("Digite a posição do aluno que deseja excluir: "))
    except ValueError:
        print("Digite um número válido!")
        return

    if posicao < 1 or posicao > len(alunos):
        print("Posição inválida!")
        return

    alunos.pop(posicao - 1)
    print("Aluno excluído com sucesso!")


def menu():
    while True:
        print("\n--- Menu ---")
        print("1 - Cadastrar Aluno")
        print("2 - Listar Alunos")
        print("3 - Atualizar Aluno")
        print("4 - Excluir Aluno")
        print("5 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            update()
        elif opcao == "4":
            delete()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


# principal
menu()