import requests

cep = input("Digite o CEP que deseja consultar: ")
complemento_endereco = input("Digite o complemento do CEP:")
url = f'https://viacep.com.br/ws/{cep}/json/'

try:
    requicao = requests.get(url)

    if requicao.status_code == 200:
        dic_requisicao = requicao.json()

        print(f'Logradouro: {dic_requisicao["logradouro"]}')
        print(f'Complemento: {dic_requisicao["complemento"]}{complemento_endereco}')
        print(f'Localidade: {dic_requisicao["localidade"]}')
        print(f'Bairro: {dic_requisicao["bairro"]}')
        print(f'Estado: {dic_requisicao["uf"]}')

    elif requicao.status_code == 404:
        print('CEP não encontrado.')
    elif requicao.status_code == 400:
        print('CEP inválido.')
    elif requicao.status_code == 500:
        print('Erro interno do servidor.')  

except ConnectionError as erro:
    print(f'Erro ao consultar o CEP: {erro}')