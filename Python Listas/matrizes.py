def criar_matriz_notas(n):
    matriz = []
    for i in range(n):
        print(f'\n Notas do aluno {i+1}')

        notas = []

        for j in range(3):
            nota = float(input('Nota: {j+1}:'))
            notas.append(nota)

        matriz.append(notas)
    return matriz        