def menu():
    print('---Menu---')
    print('1- Adição')
    print('2- Subtração')
    print('3- Multiplicação')
    print('4- Divisão')
    opcao = int (input("Escolha um numero: "))
    return opcao

def entrada():
    print('---entrada---')
    num = int(input('Numuro: '))
    return num

def adicao(n1,n2):
    print('---Adição---')
    return n1 + n2

def subtracao(n1,n2):
    print('---Subtração---')
    return n1 - n2  

def multiplicacao(n1,n2):
    print('---Multiplicação---')
    return n1 * n2

def divisao(n1,n2):
    print('---Divisão---')
    return n1 / n2
    
def imprimir(resultado):
    print('---Imprimir---')
    print('================')
    print(f'Resultado: {resultado}')
    print('================')
    