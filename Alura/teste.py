# nome = ['ana', 'carlos']

# nome.append('enzo')
# nome.append('Laura')
# nome.append('kaua')
# nome.remove('enzo')
# nome.count('kaua')
# print(nome)

'''
Crie um programa em Python para cadastrar 5 nomes de jogos em uma lista.
O programa deve mostrar todos os jogos cadastrados, permitindo também, adicionar
e remover um novo jogo, e ordenar a lista (jogos). Ao final, exibir a lista
atualizada.
'''
'''
jogos = []
 
def nome_jogos():
    for i in range(5):
        nome = input('Digite um jogo: ')
    jogos.append(nome)

def lista_inicial():
    print('\n --- Lista Inicial ---')
    print(jogos)
 
    novo_jogo = input('Novo Jogo: ')
    jogos.append(novo_jogo)
 
    print('===========================')

def lista_atulizada():
    print('\n --- Lista Atualizada ---')
    print(jogos)
 
    remover = input('Jogo para remover: ')
    if remover in jogos: #validação
        jogos.remove(remover)
 
    jogos.sort()
 
    print('===========================')


def lista_final():
    print('\n --- Lista Final ---')
    print(jogos)
    for jogo in jogos:
        print(jogo)
    

nome_jogos()
lista_inicial()
lista_atulizada()
lista_final()
'''
'''
jogos = []


def cadastrar_jogos():
    for i in range(5):
        nome = input(f'Digite o nome do Jogo {i + 1}: ')
        jogos.append(nome)
    print('\n✅ Jogos cadastrados com sucesso!\n')


def listar_jogos():
    if len(jogos) == 0:
        print('\n⚠️ Nenhum jogo cadastrado!\n')
    else:
        print('\n--- RANKING DE JOGOS ---')
        for i in range(len(jogos)):
            print(f'{i + 1} - {jogos[i]}')
        print()


def adicionar_jogo():
    nome = input('Digite o nome do novo jogo: ')
    jogos.append(nome)
    print('✅ Jogo adicionado com sucesso!\n')


def remover_jogo():
    nome = input('Digite o jogo que deseja remover: ')
    if nome in jogos:
        jogos.remove(nome)
        print('\n✅ Jogo removido com sucesso!\n')
    else:
        print('⚠️ Jogo não encontrado!\n')


def ordenar_jogos():
    jogos.sort()
    print('✅ Lista ordenada com sucesso!\n')


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

        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('⚠️ Digite apenas números!\n')
            continue

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
            print('⚠️ Opção inválida!\n')


# Principal
menu()
'''

def qtde_alunos():
    qtde = 0
    while qtde < 1:
        qtde = input("Qual a quantidade de alunos: ")
    if qtde < 1:
        print("Essa quantidade tem que ser maior que ZERO!")
    return qtde

qtde_alunos = qtde_alunos()     

def preencher_notas(alun):
        notas = []
        for i in range(alun):
            print(f"Alunos {i+1}")
            nota = float(input("Nota: "))
            nota.append(nota)
            return notas

lista_notas = preencher_notas()        

def calcular_media(alunos, notas):
    total_notas = 0
    for nota in notas:
        total_notas = total_notas + notas
    media = total_notas / len(notas)
    print(f"A media dos alunos é {media:.1f}")

def alunos_abaixo_media(notas):
     alunos_abaixo = []
     for nota in notas:
       if nota < 6:
        alunos_abaixo.append(nota)
        return alunos_abaixo 

alun_abaixo = alunos_abaixo_media(lista_notas)
print(alun_abaixo)

def qtde_alunos_abaixo(abaixo):
    print(f"Quantidade de alunos abaixo de média é {len(abaixo)}")

qtde_alunos_abaixo(alun_abaixo)    

