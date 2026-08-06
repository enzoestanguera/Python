'''
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
'''

def obter_dados():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    return nome, idade, peso, altura

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 19:
        return "baixo do peso ideal"
    elif imc <= 25:
        return "peso normal"
    elif imc <= 30:
        return "sobrepeso"
    else:
        return "obesidade"

nome, idade, peso, altura = obter_dados()
imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print("\n===== RELATÓRIO =====")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")