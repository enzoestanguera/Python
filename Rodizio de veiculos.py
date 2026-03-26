'''
Exercício 4 Rodízio de Veículos (São Paulo)
Escreva um programa em Python que solicite ao usuário o último dígito da placa de um veículo (um número inteiro de 0 a 9) e o dia da semana (também representado por um número de 1 a 5), considerando apenas dias úteis:
1 → Segunda-feira
2 → Terça-feira
3 → Quarta-feira
4 → Quinta-feira
5 → Sexta-feira
 
O programa deve utilizar if, elif e else para verificar se o veículo está impedido de circular naquele dia, de acordo com as regras do rodízio de veículos da cidade de São Paulo:
Segunda-feira (1): placas terminadas em 1 e 2
Terça-feira (2): placas terminadas em 3 e 4
Quarta-feira (3): placas terminadas em 5 e 6
Quinta-feira (4): placas terminadas em 7 e 8
Sexta-feira (5): placas terminadas em 9 e 0
O programa deve exibir uma das seguintes mensagens:
"Rodízio ativo: veículo não pode circular"
"Dia ou placa inválidos" (caso os valores informados estejam fora dos intervalos esperados)
Requisitos:
Utilizar  if, else if e else ou match-case.
Validar se o dia está entre 1 e 5.
Validar se o dígito da placa está entre 0 e 9.
Exemplo de execução:
Digite o último dígito da placa: 4
Digite o dia da semana (1 a 5): 2
Rodízio ativo: veículo não pode circular
 
'''
ultimodigito = int(input('digite o ultimo digito da sua placa: '))
diadasemana = int(input('qual o dia da semana: '))

match diadasemana:
     case 1:
          print('segunda')
     case 2:
          print('terça')     
     case 3:
          print('quarta')   
     case 4:     
          print('quinta')
     case 5:
          print('sexta')

if ultimodigito >=0 and ultimodigito <= 2 and diadasemana == 1:   
     print(f'rodizio ativo {1,  2} não pode circular')  
elif ultimodigito >=3 and ultimodigito <= 4 and diadasemana == 2:
     print(f'rodizio ativo {3, 4}')  
elif ultimodigito >=5 and ultimodigito <= 6 and diadasemana == 3:
     print(f'rodizio ativo {5, 6}')  
elif ultimodigito >=7 and ultimodigito <=8 and diadasemana == 4:
      print(f'rodizio ativo {7, 8}')
else:
    print(f'rodizio ativo {9, 0}')             