jogos = []
 
def cadastrar jogos():
    for i in range(5):
        nome = input(f'Digite o nome do Jogo {i+1}: ')
        jogos.append(nome)
    print('\n ✅ Jogos cadastrados com sucesso! \n')
 
def listar_jogos():
    if len(jogos) == 0:
        print('\n ⚠️ Nenhum jogo cadastrado! \n')
    else:
        print('\n --- RANKING de JOGOS ---')
        for i in range(len(jogos)):
            print(f'{i + 1} - {jogos[i]}')
 
def adicionar_jogo():
    nome = input('Digite o nome do novo Jogo: ')
    jogos.append(nome)
    print('✅ Jogo adicionado com sucesso! \n')
 
def remover_jogo():
    nome = input('Digite o jogo que deseja remover: ')
    if nome in jogos:
        jogos.remove(nome)
        print('\n ✅ Jogo removido com sucesso! \n')
    else:
        print('Jogo não encontrado!\n')
 
def ordenar_jogos():
    jogos.sort()
    print('✅ Lista ordenada com sucesso! \n')
 
 
def menu():
    opcao = 0
 
    while opcao != 6:
        print('=== MENU ===')
        print('1 - Cadastrar jogos')
        print('2 - Listar jogos')
        print('3 - Adicionar jogo')
        print('4 - Remover jogo')
        print('5 - Ordenar jogos')
        print('6 - Sair')
        opcao = int(input('Escolha uma opção: '))
 
        if opcao == 1:
            cadastrar_jogos()
        elif opcao == 2:
            listar_jogos()
        elif opcao == 3:
            adicionar_jogo()
        elif opcao == 4:
            remover_jogo()
        elif opcao == 5:
            ordenar_jogos()
        elif opcao == 6:
            print('Programa encerrado!')
        else:
            print('Opção inválida!\n')
 
#Principal
menu()    