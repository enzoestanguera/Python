'''
todos_nomes = []
nomes_vogal = []
nomes_consoante = []
 
vogais = "AEIOUaeiou"
print("Escreva 5 nomes:")
for i in range(5):
    nome = input(f"Nome {i+1}: ")
    todos_nomes.append(nome)
   
    if nome[0] in vogais:
        nomes_vogal.append(nome)
    else:
        nomes_consoante.append(nome)
 
print(f"Lista com todos os nomes: {todos_nomes}")
 
print(f"\nNomes iniciados com VOGAL: {nomes_vogal}")
print(f"Quantidade: {len(nomes_vogal)}")
 
print(f"\nNomes iniciados com CONSOANTE: {nomes_consoante}")
print(f"Quantidade: {len(nomes_consoante)}")

'''

list = []

while True:
    item = input(f"Digite item( ou 'sair' para Finalizar):")

    if item.lower() == 'sair':
        break

    list.append(item)

    print('\n')
