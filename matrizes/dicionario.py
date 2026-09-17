#dicionario
aluno = {
    "nome" : "Pedro",
    "idade": 20,
    "curso": "ads"
}
print(aluno)

#pegar a informação no dic
aluno['nome']
aluno['idade']
aluno['curso']

#mudar um valor no dic
aluno['nome'] = "Gabriel"
print(aluno)

produto = {
    "nome": "Macbook",
    "preço": 20000,
    "estoque": 10,
    "disponivel" : True
}

print(produto)
print(produto['nome'])
print(produto['preço'])
print(produto['estoque'])
print(produto['disponivel'])

#metodo get(pegar um elemento):
print(produto.get('nome'))
print(produto.get('preço'))
print(produto.get('estoque'))
print(produto.get('disponivel'))

#adicionar um novo elemnto
produto['marca'] = 'apple'
print(produto)

#alterando algo existente no dic:
produto['preço'] = 18000
print(produto)

#retirar um item no dic com pop
produto.pop('marca')
print(produto)

#retirar um elemento com a função del:
del produto['disponivel']
print(produto)

#tamanho no dicionario:
print(len(produto))

#verificar se tem um item no dicionario:
if 'nome' in produto:
    print('Existe')
else:
    print('Não existe')

produto = {
    "nome": "Macbook",
    "preço": 20000,
    "estoque": 10,
    "disponivel" : True
}

#metodo keys:
produto.keys()

for chave in produto.keys():
    print(chave)

#metodo values:
produto.values()

for valor in produto.values():
    print(valor)

#metodo items:
produto.items()

for chave, valor in produto.items():
    print(f"{chave} : {valor}")

#metodo update(atualiza o dicionario):
produto.update({'nome': 'Lucas', 'estoque': 80})
print(produto)

#metodo clear(apaga todos os elementos do dicionario):
produto.clear()
print(produto)