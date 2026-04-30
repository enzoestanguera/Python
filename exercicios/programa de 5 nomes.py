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

lista = []
i = 0

while True:
    item = input("Digite um item (ou 'sair' para finalizar): ")

    if item.lower() == 'sair':
        break

    lista.append(item)
    print()

for i in range(len(lista)):
    print(f"{i + 1}. {lista[i]}")