def matriz():
    matrizes = [[0,0,0], [0,0,0], [0,0,0]]
    for l in range(3):
        for c in range(3):
            while True:
                try:
                    matrizes [l] [c] = int (input(f"Digite a posição [{l}] [{c}]"))
                    break
                except ValueError:
                    print("Digite apenas numeros validos")
                except ZeroDivisionError:
                    print("O valor não pode ser zero")
                finally:
                        print("finalizando ensaio de preenchimento matrizx")
        print("-="*30)
        for l in range(3):
            for c in range(3):
                print(f"[{matrizes [l] [c]:^5}]", end="")
            print()
matriz()            