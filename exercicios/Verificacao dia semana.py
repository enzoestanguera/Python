'''
    Exercício 1 Verificação dia da semana
 
1-Escreva um programa em Python que solicite ao usuário a entrada de um número inteiro de 1 a 7, representando os dias da semana, conforme a tabela abaixo:
1 → Domingo
2 → Segunda-feira
3 → Terça-feira
4 → Quarta-feira
5 → Quinta-feira
6 → Sexta-feira
7 → Sábado
 
O programa deve utilizar estruturas condicionais (match-case) para  verificar o valor informado e exibir uma das seguintes mensagens:
 
"Fim de semana" para os dias 1 (Domingo) e 7 (Sábado)
"Dia comercial" para os dias de 2 a 6 (Segunda a Sexta)
"Dia inválido" caso o número informado não esteja entre 1 e 7
Requisitos:
O programa deve ler o valor pelo teclado.
Validar a entrada do usuário.
    '''      

dia = int(input('qual dia é hoje ? '))

match dia:
    case 1:
          print('domingo')
          print('fim de semana')
    case 2:
        print('segunda')
        print ('Dia comercial')
    case 3:
          print('terça') 
          print('dia comercial')
    case 4:
          print('quarta')
          print ('dia comercial')
    case 5:
          print('quinta')
          print('dia comercial')
    case 6:
          print('sexta')
          print('Dia comercial')
    case 7:
         print ('fim de semana')                
    case _:
        print(f'dia invalido {dia} dia não reconhecido')    

    