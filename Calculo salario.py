''' Cálculo de Salário com Comissão
Enunciado: Uma empresa paga um salário fixo de R$ 2.000,00 mais uma comissão de 15% sobre o total de vendas efetuadas pelo vendedor. Receba o total de vendas do mês e exiba o salário final.
Entrada: Total de vendas (double).
Processamento: total = 2000 + (vendas * 0.15).
Saída: Salário final formatado.'''

totaldevendas = float(input("valor total das vendas"))

totaldevendas * 0.15 + 2000

salariofinal = totaldevendas * 0.15 + 2000

print("Seu salario final:", salariofinal)
