# Um set é uma coleção que:
# - Não permite elementos duplicados
# - Não possui índices
# - Permite adicionar e remover elementos
# - Possui operações como união, interseção e diferença


# 1. CRIANDO UM SET
# Criando um set diretamente com {}
nomes = {"Pedro", "Enzo", "Larissa"}

print("Set de nomes:", nomes)


# 2. SET VAZIO
# CUIDADO:
# {} cria um dicionário, e NÃO um set.
# Para criar um set vazio, usamos set()
conjunto_vazio = set()

print("Set vazio:", conjunto_vazio)


# 3. SET() — TRANSFORMANDO UMA LISTA EM SET
# Podemos transformar uma lista em set.
# Os valores repetidos serão eliminados automaticamente.

lista = [1, 2, 2, 3, 3, 4, 5]

numeros = set(lista)

print("Lista:", lista)
print("Set:", numeros)

# Outro exemplo:
nomes_lista = ["Enzo", "Pedro", "Enzo", "Larissa", "Pedro"]

nomes_unicos = set(nomes_lista)

print("Nomes sem repetição:", nomes_unicos)


# 4. ADD() — ADICIONAR ELEMENTO
# O add() adiciona UM elemento ao set.

frutas = {"maçã", "banana", "laranja"}

frutas.add("uva")

print("Depois do add():", frutas)

# Se tentarmos adicionar um elemento que já existe,
# nada acontece porque o set não aceita duplicados.

frutas.add("uva")

print("Tentando adicionar uva novamente:", frutas)


# 5. DISCARD() — REMOVER ELEMENTO
# O discard() remove um elemento do set.

frutas.discard("banana")

print("Depois do discard():", frutas)


# Se tentarmos remover algo que NÃO existe,
# o discard() não gera erro.

frutas.discard("abacaxi")

print("Tentando remover abacaxi:", frutas)


# 6. REMOVE() — REMOVER ELEMENTO
# O remove() também remove um elemento.

numeros = {10, 20, 30, 40}

numeros.remove(30)

print("Depois do remove():", numeros)


# DIFERENÇA ENTRE discard() E remove():
#
# discard() -> se o elemento não existir, não acontece nada.
#
# remove() -> se o elemento não existir, o Python gera um erro.


# 7. UNION() — UNIÃO
# O union() junta dois sets.
# Elementos repetidos aparecem apenas uma vez.

A = {1, 2, 3}
B = {3, 4, 5}

resultado = A.union(B)

print("A:", A)
print("B:", B)
print("União:", resultado)

# Resultado:
# {1, 2, 3, 4, 5}

# 8. INTERSECTION() — INTERSEÇÃO

# O intersection() mostra os elementos
# que existem nos DOIS sets.

A = {1, 2, 3}
B = {3, 4, 5}

resultado = A.intersection(B)

print("A:", A)
print("B:", B)
print("Interseção:", resultado)

# Resultado:
# {3}


# Outro exemplo:

alunos_python = {"Enzo", "Pedro", "Lucas"}
alunos_java = {"Enzo", "Maria", "Lucas"}

resultado = alunos_python.intersection(alunos_java)

print("Alunos que estudam Python e Java:", resultado)

# Resultado:
# {'Enzo', 'Lucas'}

# 9. DIFFERENCE() — DIFERENÇA

# O difference() mostra os elementos que existem
# no PRIMEIRO set, mas NÃO existem no segundo.

A = {1, 2, 3}
B = {3, 4, 5}

resultado = A.difference(B)

print("A:", A)
print("B:", B)
print("Diferença A - B:", resultado)

# Resultado:
# {1, 2}


# IMPORTANTE:
# difference() NÃO altera o set original.
#
# Por isso, normalmente guardamos o resultado
# em uma variável.


# 10. EXEMPLO COMPLETO

# Set de pessoas

x = {"Pedro", "Enzo", "Larissa"}

# Set de empresas

y = {"Apple", "Microsoft", "Google"}


# Diferença:
# Pessoas que estão em X, mas não estão em Y.

resultado = x.difference(y)

print("X:", x)
print("Y:", y)
print("Diferença:", resultado)


# RESUMO DOS PRINCIPAIS COMANDOS
# set()
# Cria um set ou transforma uma lista em set.

# add()
# Adiciona um elemento.

# discard()
# Remove um elemento sem gerar erro caso ele não exista.

# remove()
# Remove um elemento, mas gera erro caso ele não exista.

# union()
# Junta dois sets.

# intersection()
# Retorna os elementos que existem nos dois sets.

# difference()
# Retorna os elementos que existem no primeiro set,
# mas não existem no segundo.

# add          -> ADICIONAR
# discard      -> DESCARTAR
# remove       -> REMOVER
# union        -> UNIR / JUNTAR
# intersection -> ELEMENTOS EM COMUM
# difference   -> DIFERENÇA
# set()        -> CONJUNTO
