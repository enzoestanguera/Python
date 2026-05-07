'''
nome = (input("Digite seu nome: "))
idade = (input("Digite sua idade: "))
pi=3.14

print(f"meu nome é {nome} e tenho {idade} anos")
print(f"O valor de pi é {pi:.2f}")

'''

import os

def fechando_programa():
    os.system('cls')
    print("Encerrando programa\n")

def opcao_invalida():
    print("O seu numero esta incorreto escolha outro!\n")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def opções():
    try:
        opção = int(input("Digite a opção desejada: "))

        if opção == 1:
            print("Ativar celular")
        elif opção == 2:
            print("Desativar celular")
        elif opção == 3:
            print("Configurar celular")
        elif opção == 4:
            fechando_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    print("1 - Ativar celular")
    print("2 - Desativar celular")
    print("3 - Configurar celular")
    print("4 - Sair\n")
    opções()

if __name__ == '__main__':
    main()

   
'''
def fechando_programa():
    print("encerrando o programa")

opcao = int(input("digite uma opção: "))

match opcao:
    case 1:
        print("Ativar troxa")
    case 2:
        print("Desativar troxa")
    case 3:
        print("Configurar troxa")
    case _:
        fechando_programa()
'''

'''
def fim_programa():
    print("Encerrando programa")
    print("""
            ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
            ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
            ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
            ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
            ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
            ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
            """)
    
def idades():
    idade = int(input("Digite sua idade: "))

    if idade <= 12:
        print("voce é criança")
    elif idade <= 18:
        print("Adolecente")
    elif idade <= 60:
        print("Adulto")
    else:
        fim_programa() 
    
idades()
'''





      


