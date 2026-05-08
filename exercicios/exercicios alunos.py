def qtde_alunos():
    print('--Quantidade de Alunos--')
    qtde = 0
    while qtde <1:
        qtde = int(input('Qtde de alunos: '))
        if qtde < 1:
            print('ESta quantidade tem que ser MAIOR que ZERO')
        return qtde

def preencher_notas(qtde):
    print('--Preeenchendo as notas--')
    notas = []
    for i in range(qtde):
        print(f'Aluno {i+1}: ')
        nota = float(input('Nota: '))
        notas.append(nota)
    return notas

def imprimir_notas(qtde_alunos, qtde):
    print('--Imprimindo as notas dos alunos... ---')

import os
def valor_errado():
    os.system('cls')
    print('O seu valor esta incorreto!')
    