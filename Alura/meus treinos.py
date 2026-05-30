def lista_capitalize():
    print("=== Lista Capitalize")


pessoa = {'Nome': 'Enzo',
         'Idade' : 18,
         'Cidade': 'São Paulo',
        }
        

def listando():
    print("Listando o Dicionario")

    pessoa['Idade'] = 21
    pessoa['Nome'] = 'davi'

    print(pessoa)

def lista_remove():
    print("Removendo Itens da lista")    
    pessoa.pop ('Cidade')
    print(pessoa)

lista_capitalize()
listando()
lista_remove()
