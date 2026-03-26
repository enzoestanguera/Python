#exemplo com numero (int)
n = int (input("numero 1: "))

match n:
    case 1:
        print(f'valor 1{n}')
    case 2:
        print(f'n valor 2 {n}')
    case 3:
        print(f'n valor 3 {n}')
    case __:
        print(f'numero invalido')