'''
def menu():
    print('---Menu---')
    print('1- Adição')
    print('2- Subtração')
    print('3- Multiplicação')
    print('4- Divisão')

    opcao = int(input("Escolha um numero: "))
    return opcao


def entrada():
    print('---entrada---')
    num = int(input('Numero: '))
    return num


def adicao(n1, n2):
    print('---Adição---')
    return n1 + n2


def subtracao(n1, n2):
    print('---Subtração---')
    return n1 - n2


def multiplicacao(n1, n2):
    print('---Multiplicação---')
    return n1 * n2


def divisao(n1, n2):
    print('---Divisão---')
    return n1 / n2


def imprimir(resultado):
    print('---Imprimir---')
    print('================')
    print(f'Resultado: {resultado}')
    print('================')


def controlador(opcao, n1, n2):
    print('---Controlador----')

    if opcao == 1:
        resultado = adicao(n1, n2)

    elif opcao == 2:
        resultado = subtracao(n1, n2)

    elif opcao == 3:
        resultado = multiplicacao(n1, n2)

    elif opcao == 4:
        resultado = divisao(n1, n2)

    else:
        opcao_errada()
        return None

    return resultado


def opcao_errada():
    print("A sua opção está errada")


opcao = menu()
n1 = entrada()
n2 = entrada()

resultado = controlador(opcao, n1, n2)

if resultado is not None:
    imprimir(resultado)
    '''


import os

pedra = "pedra"
papel = "papel"
tesoura = "tesoura"

Jogador1 = input("Escolha uma opção: ").lower()
jogador2 = input("Vez do Jogador 2: ").lower()

def Escolhasuavez():

    while True:
        if Jogador1 == jogador2:
            print("Empate ")
            break
        elif Jogador1 == "papel" and jogador2 == "pedra":
            print("Jogador 1 venceu")
            break
        elif Jogador1 == "pedra" and jogador2 == "papel":
            print("jogador 2 venceu") 
            break
        elif Jogador1 == "tesoura" and jogador2 == "papel":
            print("jogador 1 venceu") 
            break
        elif Jogador1 == "papel" and jogador2 == "tesoura":
            print(" jogador 2 venceu")
            break            
        elif Jogador1 == "pedra" and jogador2 == "tesoura":
            print("jogador 1 venceu")
            break
        elif Jogador1 == "tesoura" and jogador2 == "pedra":
            print("jogador 2 venceu")
        else:
            opcao_errada()
            
            break

def opcao_errada():
    os.system("cls")
    if Jogador1 == opcao_errada and jogador2 == opcao_errada:
        print("opção errada escolha outra opção!")
        Escolhasuavez()

def excutar():
    Escolhasuavez()
excutar()
    

   




