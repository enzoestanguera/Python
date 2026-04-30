numero = int(input('Escolha um numero (1-10): '))

if 1 <= numero <= 10:
    print(f"Tabuada do {numero}:")
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
else:
    print("Número inválido! Escolha 1-10.")
    i = 1
    while i <=10:
        print(f"{numero} x {i} = {numero * i}")
