'''
Catalogo de tenis
'''

catalogo_tenis = {  "Air force One": ["Tenis Premium", 500.00,["Loja fisica", "Loja Virtual"]],
                    "Adidas Samba" :["Tenis Padrao", 750.00,["Loja do Exterior", "Loja fisica"]],
                    "Nike Dn" : ["Tenis Premium", 1500, ["Loja do Exterior", "Loja fisica"]]
              }

def exibir_menu():
    print("---Catalogo de Tenis Premium---")
    print("1. Listar todos os Tenis")
    print("2. Adicionar um novo Tenis")
    print("3. Atualizar um Tenis")
    print("4. Deletar Tenis")
    print("5. Sair")

def lista_tenis(catalogo):
    if len(catalogo) == 0:
        print("\n O catalogo esta vazio")
        return

    print("\n---Catalago de Tenis---")

    for nome in catalogo:
        dados = catalogo[nome]
        categoria = dados[0]
        preco = dados[1]
        plataformas = dados[2]

        print(f'Tenis: {nome}')
        print(f'Categoria: {categoria}')
        print(f'Preço: {preco}')
        print(f'Plataformas: ', end=" ")

        for p in plataformas:
            print(p, end="")

        print("\n" + "-" * 30)

def cadastrar_sapato(catalogo, nome, categoria, preco, plat1, plat2):
    if nome in catalogo:
        return False

    lista_plataformas = [plat1, plat2] 

    catalogo[nome] = [categoria, preco, lista_plataformas]
    return True


def atualizar_tenis(catalogo, nome, nova_categoria, novo_preco, nova_p1, nova_p2 ):
    if nome not in catalogo:
        return False
    nova_plataformas = [nova_p1, nova_p2]
    catalogo[nome] = [nova_categoria, novo_preco, nova_plataformas]
    return True

def deletar_tenis(catalogo, nome):
    if nome not in catalogo:
        return False
    del catalogo[nome]
    return True

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma Opção: ")

        if opcao =="1":
            lista_tenis(catalogo_tenis)
        elif opcao == "2":
            print("\n ---Cadastrar um Novo Tenis---")
            nome = input("Digite o nome do tenis: ")
            categoria = input("Digite a Categoria do Tenis: ")
            preco = float (input("Digite o valor do Tenis: "))
            p1 = input("Digite a Plataforma 1: ")
            p2 = input("Digite a Plataforma 2: ") 

            cadastrar = cadastrar_sapato(catalogo_tenis, nome , categoria, preco, p1, p2)

            if cadastrar:
                print("[SUCESSO] : Tenis Cadastrado")
            else:
                print("[ERRO] : Tenis não cadastrado")
        elif opcao == "3":
            print("\n ---Atualizar um Tenis---")
            nome = input("Digite o nome do tenis que deseja atualizar: ")

            if nome in catalogo_tenis:
                categoria = input("Digite a Nova Categoria: ")
                preco = float(input("Digite o novo Valor: "))
                p1 = input("Digite a Nova Plataforma 1: ")
                p2 = input("Digite a Nova Plataforma 2: ")

                atualizou = atualizar_tenis(catalogo_tenis,nome, categoria, preco, p1, p2)
                if atualizou:
                    print("[SUCESSO] : Tenis Atualizado")
                else:
                    print("[ERRO] : Tenis não encontrado no Catalogo")

            elif opcao =="4":
                print("\n ---Deletar um Tenis---")
                nome = input("Digite o nome do tenis que deseja remover: ")

                deletou = deletar_tenis(catalogo_tenis, nome )   
                if deletou:
                    print("[SUCESSO] : '{nome}' foi removido do Catalogo!")
                else:
                    print(f"[ERRO]: Tenis '{nome}' não foi encontrado no Catalogo!")

            elif opcao == "5":
                print("Encerrando o SISTEMA")     
            break
        else:
            print('[ERRO]: Opção invalida! escolha uma opção de 1 a 5')
main()

