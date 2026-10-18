import csv
import requests

arquivo = "historico_cep.csv"

# Solicita o CEP ao usuário e após ele fazer isso ele vai remover traços e espaços antes da consulta.
def obter_cep():
    cep = input("Digite o CEP que deseja consultar: ")
    cep = cep.replace("-", "").strip()  # Remove traços e espaços em branco
    return cep

#A Função serve para consultar os dados do CEP na API VIACEP indentifica o 200 como sucesso, 404 como não encontrado e 400 invalido, 500 como erro interno do servidor
#apos a consulta ele retorna os dados do endereço e caso ele não encontre ou ocorra algum erro ele vai retornar como vazio     
def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'

    try:
        requisicao = requests.get(url)

        if requisicao.status_code == 200:
            dic_requisicao = requisicao.json()
            return dic_requisicao
        elif requisicao.status_code == 404:
            print('CEP não encontrado.')
        elif requisicao.status_code == 400:
            print('CEP inválido.')
        elif requisicao.status_code == 500:
            print('Erro interno do servidor.')  
    except ConnectionError as erro:
        print(f'Erro ao consultar o CEP: {erro}')
    return None    

# A Função vai salvar os dados do endereço consultado em um arquivo CSV chamado "historico_cep.csv".
#vai verificar se o arquivo já existe, caso não exista ele cria o arquivo e adiciona o cabeçalho, caso exista ele apenas adiciona os dados do endereço no final do arquivo.
#vai procurar o cep, logradouro, complemento, bairro, localidade e uf no dicionário retornado pela API 
#e caso algum desses campos não exista ele vai adicionar uma string .
def salvar_historico(dados_endereco):
    if not dados_endereco:
        return

    colunas = ["cep", "logradouro", "complemento", "bairro", "localidade", "uf"]
    arquivo_existente = False

    try:
        with open(arquivo, "r", encoding="utf-8") as arquivo_csv:
            arquivo_existente = True
    except FileNotFoundError:
        arquivo_existente = False

    try:
        with open(arquivo, mode="a", newline="", encoding="utf-8") as arquivo_csv:
            escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=colunas)

            if not arquivo_existente:
                escritor_csv.writeheader()

            dados_endereco_filtrados = {coluna: dados_endereco.get(coluna, "") for coluna in colunas}
            escritor_csv.writerow(dados_endereco_filtrados)

            print("Dados do endereço salvos no histórico com sucesso.")
    except Exception as erro:
        print(f'Erro ao salvar o histórico: {erro}')

# Essa Função serve para exibir o histórico de CEPs consultados, lendo os dados do arquivo CSV "historico_cep.csv" e exibindo-os no console.
#o with open ele vai abrir o arquivo em modo leitura e vai criar um objeto leitor_csv que vai ler o arquivo e armazenar os dados em uma lista chamada historico.
#caso ele não ache o arquivo ele vai exibir a mensagem "Nenhum histórico encontrado." e caso ocorra algum erro ele vai exibir a mensagem "Erro ao exibir o histórico: {erro}".
def exibir_historico():
    try:
        with open(arquivo, mode="r", encoding="utf-8") as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            historico = list(leitor_csv)

            if historico:
                print("Histórico de CEPs consultados:")
                for registro in historico:
                    print(f'CEP: {registro["cep"]}, Logradouro: {registro["logradouro"]}, '
                          f'Complemento: {registro["complemento"]}, Bairro: {registro["bairro"]}, '
                          f'Localidade: {registro["localidade"]}, Estado: {registro["uf"]}')
            else:
                print("Nenhum histórico encontrado.")
    except FileNotFoundError:
        print("Nenhum histórico encontrado.")
    except Exception as erro:
        print(f'Erro ao exibir o histórico: {erro}')

#Principal função do programa, vai exibir um menu com opções para consultar CEP, exibir histórico de CEPs consultados ou sair do programa.
def main():
    while True:
        print("\n----Menu----")
        print("1. Consultar CEP")
        print("2. Exibir histórico de CEPs consultados")
        print("3. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cep = obter_cep()
            dados_endereco = consultar_cep(cep)
            if dados_endereco:
                print(f'Logradouro: {dados_endereco["logradouro"]}')
                print(f'Complemento: {dados_endereco["complemento"]}')
                print(f'Localidade: {dados_endereco["localidade"]}')
                print(f'Bairro: {dados_endereco["bairro"]}')
                print(f'Estado: {dados_endereco["uf"]}')
                salvar_historico(dados_endereco)
        elif opcao == "2":
            exibir_historico()
        elif opcao == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

#executa a função principal do programa quando o arquivo é executado diretamente.
if __name__ == "__main__":
    main()            