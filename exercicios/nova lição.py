'''
Cálculo de Conta de Energia 2026
 
Escreva um programa para calcular o valor de uma conta de energia elétrica de
um consumidor com base no consumo de kWh. O programa deve receber o consumo de energia e
calcular o valor a pagar. Ao final, deve imprimir a conta detalhada (consumo, tarifa
aplicada, valor total a pagar...)
 
 
Regras de Negócio:
 
Consumo < 150 kWh: R$ 0,75 por kWh.
 
Consumo entre 150 e 500 kWh: R$ 0,95 por kWh.
 
Consumo acima de 500 kWh: R$ 1,20 por kWh.
 
Taxa Mínima (Disponibilidade): R$ 45,00 (se o cálculo do consumo for inferior a
este valor, o consumidor paga o mínimo).
'''
consumo = int(input("digite o valor de  energia consumida em kwh"))

if consumo <150:
    tarifa = 0.75

elif 150 <= consumo <= 500:
    tarifa = 0.95
else:
    tarifa = 1.20

valor_final = consumo * tarifa

if valor_final <= 45:
    valor_final = 45
    print ("aplicada a taxa minimo de 45 reais")
else:
    valor_final = valor_final

print (tarifa , valor_final , consumo) 

