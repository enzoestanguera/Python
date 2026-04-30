#adição de lista
#sem repetição 

'''
salarios = [0,0, 0, 0 ]
soma = 0

i = 0 #variavel que sera usada como indice da lista
while i<4:
    if salarios [i] < media:
        print(f" abaixo da media: R$  {salarios [i]:.2f}")

media = soma / 4

print('---------------')
print(f'Media Salarial: R$ {media:.2f}')
print('---------------')

i = 0 #variavel que sera usada como indice da lista
while i<4:
    if salarios [0] < media:
        print(f" abaixo da media: R$  {salarios [i]:.2f}")


Estrutura de repetição FOR
- Estrutura definida (qtde de repetições conhecidas)
 
- Sintaxe:
for <variavel> in <sequência>:
    <bloco de código>
 
- Método append()
'''
'''
Estrutura de repetição FOR
- Estrutura definida (qtde de repetições conhecidas)
 
- Sintaxe:
for <variavel> in <sequência>:
    <bloco de código>
 
- Método append()
'''
'''
salarios = [] #criando uma lista vazia
soma = 0
 
qtde_salarios = int(input('Qtde de salários: '))
 
for i in range(qtde_salarios):
    salario = float(input('Salário: R$ '))
    soma += salario
    salarios.append(salario)
 
media = soma / qtde_salarios
 
print('-------------------------------')
print(f'Média Salarial: R$ {media:.2f}')
print('-------------------------------')
 

print('Salários ABAIXO da média:')
for salario in salarios:
    if salario < media:
        print(f'  --> R$ {salario:.2f}')
 

print('Salários ACIMA da média:')
for salario in salarios:
    if salario > media:
        print(f'  --> R$ {salario:.2f}')
 '''


 #Solicite ao usuário o número de funcionários
 #Altere os salários na lista
 #Imprimir os salários acima da média
 
#TO DO
# Adicionar os salários abaixo da média em uma lista
#Adicionar os salários acima da média em uma outra lista

 
salarios = []
soma = 0 

for i in range(4):
    salario = float(input("Salario: R$ "))
    soma =+ salario
    salarios.append(salario)

    media = soma / 4 

print('------------------')
print('')


