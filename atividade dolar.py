'''1. Conversor de Moedas
Enunciado: Crie um programa que receba um valor em Reais (R$) e a cotação atual do Dólar. 
O programa deve exibir quanto esse valor representa em Dólares (US$).
Entrada: Valor em reais e cotação do dólar.
Processamento: dolar = reais / cotacao.
Saída: Valor convertido.'''

valoreal = float(input("o seu valor em real:"))
valorcotacao = float(input("quanto é a cotação do dolar?"))

dolar = valoreal / valorcotacao

print(f"valor do dolar:{dolar:.2f}")






