

nome = input('Nome do vendendor: ')
salario = float(input('Salario fixo: '))
vendas = float(input('Total de vendas: '))

print('Periodo de Vendas')
print(' 1 - Segunda a quarta')
print('2 - Quinta a sexta')
print('3 - Sabado e domingo')
opcao = int(input('Escolha um Periodo: '))


if opcao == 1:
    comissao = vendas * 0.20
elif opcao == 2:
    comissao = vendas * 0.15
elif opcao == 3:
    comissao = vendas * 0.10
else:
    print('Opção inválida')
    comissao = 0 


total = salario + comissao

print(f'Vendedor: {nome}')
print(f'Comissão: {comissao}')
print(f'Salario: R$ {salario}')



 