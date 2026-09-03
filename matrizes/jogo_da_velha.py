def jogo_da_velha():
    # Cria a matriz 3x3
    tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    jogador_atual = "X"

    while True:
        # Exibe o resultado da matriz
        print("\n" + "-=" * 15) #pula para a linha de baixo e multiplica -= 15 vezes
        for l in range(3):
            for c in range(3):
                print(f"[{tabuleiro[l][c]:^5}]", end="") # centrliza na matriz e coloca dois espaços de cada lado para deixar a estetica mais bonita, 
            print() #end foi usado para a matriz nhão ficar em formato vertical
        print("-=" * 15)

        # Entrada e Tratamento de Erros
        while True:
            try:
                print(f"\nVez do Jogador [{jogador_atual}]")
                linha = int(input("Digite a linha (0 a 2): "))
                coluna = int(input("Digite a coluna (0 a 2): "))

                # não aceita indices maior ou menor  que 0,1,2
                if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                    print("Posição inválida! Digite números entre 0 e 2.")
                    continue#renicia o loop

                # Validação para não sobrescrever uma jogada antiga
                if tabuleiro[linha][coluna] != " ":#ele vai buscar se a posição ja foi usada no terminal anteriormente
                    print("Essa posição já está ocupada! Escolha outra.")#se ja foi usado ele vai voltar e pedir pra escolher outra posição
                    continue

                # Quebra o loop de entrada
                break

            except ValueError:
                print("Entrada inválida! Digite apenas números inteiros.")

        # Marca a jogada no tabuleiro
        tabuleiro[linha][coluna] = jogador_atual

        # Alterna o jogador para a próxima rodada
        if jogador_atual == "X":#enquanto o jogador X não jogar a O não poderá jogar
            jogador_atual = "O"
        else:
            jogador_atual = "X"


# Executa o jogo
jogo_da_velha()