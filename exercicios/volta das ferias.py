nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print(f'\n{nome} seu IMC é: {imc:.2f}')

if imc < 19:
    print(f'{nome} você esta baixo do peso ideal')
elif imc <=25:
    print(f'{nome} você esta com o peso normal')   
elif imc <=30:
    print(f'{nome} você esta com sobrepeso')
else:
    print(f'{nome} você esta com obesidade')