def criar_matriz_notas(n):
    matriz = []
    for i in range(n):
        print(f'\nNotas do aluno {i+1}')

        notas = []
        for j in range(3):
            nota = float(input(f'Nota {j+1}: '))
            notas.append(nota)

        matriz.append(notas)
    return matriz        

def nome_alunos(n):
    nomes = []
    for i in range(n):
        nome = input(f"Nome {i+1}: ")
        nomes.append(nome)
    return nomes

def calcular_medias(matriz):
    medias = []
    for linha in matriz:
       soma = 0 
       for nota in linha:
           soma+=nota
           media = soma/len(linha)
           medias.append(media)
    return medias

def mostrar_resultados(nomes, medias):
    for i in range(len(nomes)):
        print(f'{nomes[i]}: media = {medias [i]:.1f}')


def buscar_maior_nomes(nomes, media):
    nome_maior = nomes[0]
    maior_media = medias[0]
    for i in range(len(medias)):
        if medias[i] > maior_media:
            nome_maior = nomes[i]
            maior_media = medias[i]
    return nome_maior, maior_media        

n_alunos = int(input('Número de Alunos: '))
lista_alunos = nome_alunos(n_alunos)
matriz_notas = criar_matriz_notas(n_alunos)
medias = calcular_medias(matriz_notas)
mostrar_resultados(lista_alunos, medias)
