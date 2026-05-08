import os

def valor_errado():
    os.system('cls')  
    print('O seu valor esta incorreto!\n')


def qtde_alunos():
    print('--Quantidade de Alunos--')
    qtde = 0

    while qtde < 1:
        qtde = int(input('Qtde de alunos: '))

        if qtde < 1:
            valor_errado()

    return qtde

def preencher_notas(qtde):
    print('--Preenchendo as notas--')
    notas = []

    for i in range(qtde):
        print(f'Aluno {i+1}: ')
        nota = float(input('Nota: '))
        notas.append(nota)
    return notas

def imprimir_notas(notas):
    print('--Imprimindo as notas dos alunos---')

    i = 1
    for nota in notas:
        print(f'Aluno: {i}')
        print(f'Nota: {nota}')
        i += 1

def calcula_media(lista_notas):
    soma=0
    for nota in lista_notas:
        soma+=nota
    media = soma/ len(lista_notas)
    return media
   

def notas_baixas(lista_notas):
    media = calcula_media(lista_notas)
    cont = 0
    for nota in lista_notas:
        if nota < media:
            cont+=1

# principal
quantidade = qtde_alunos()
lista_notas = preencher_notas(quantidade)
media = calcula_media
imprimir_notas(lista_notas)
print(f'Quantidade: {notas_baixas(lista_notas)}')