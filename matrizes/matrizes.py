'''
Gestão de Inventário de uma Loja de Games (versão simplificada)
'''

# Estrutura principal: Dicionário onde a chave é o nome do Jogo
# e o valor é uma LISTA contendo as informações do jogo
# [categoria, preco, [LISTA de PLATAFORMAS]]

catalogo_games = {
    "Minecraft" : ["Sandbox", 99.50, ["PC", "Mobile"]],
    "Hades" : ["Roguelike", 79.99, ["PC", "Switch"]]
}

def exibir_menu():
    print('\n --- SISTEMA 1TDSPF GAMES ---')
    print('1. Listar todos os jogos')
    print('2. Adicionar novo jogo')
    print('3. Sair')

def listar_jogos(catalogo):
    
    if len(catalogo) == 0:
        print('\n O catálogo está vazio.')
        return

    print('\n --- CATALOGO de JOGOS ---')
    
    for nome in catalogo:
        dados = catalogo[nome]
        categoria = dados[0]
        preco = dados[1]
        plataformas = dados[2] #lista de plataformas

        print(f'Jogo: {nome}')
        print(f'|-- Categoria: {categoria}')
        print(f'|-- Preço: {preco}')
        print(f'|-- Plataformas: ', end="")
        
        for p in plataformas:
            print(p, end=" - ")
        
        print("\n" + "-" * 30)


def cadastrar_jogo(catalogo, nome, categoria, preco, plat1, plat2):
    if nome in catalogo:
        return False
    
    lista_plataformas = [plat1, plat2]

    catalogo[nome] = [categoria, preco, lista_plataformas]

    return True



def main():
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            listar_jogos(catalogo_games)
        elif opcao == "2":
            print('\n --- CADASTRO de um NOVO JOGO ---')    
            nome = input('Nome do Jogo: ')
            categoria = input('Categoria: ')
            preco = float(input('Preço: '))
            p1 = input('Plataforma 1: ')
            p2 = input('Plataforma 2: ')
            
            cadastro = cadastrar_jogo(catalogo_games, nome, categoria, preco, p1, p2)

            if cadastro:
                print('[SUCESSO] : Jogo Cadastrado!')
            else:
                print('[ERRO]: Jogo já cadastrado!')
        elif opcao == "3":
            print('\n Encerrando o SISTEMA')
            break
        else:
            print('[ERRO]: Opção inválida! Escolha uma opção entre 1 e 3: ')


#Principal
main()