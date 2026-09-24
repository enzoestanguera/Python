#1) limpa duplicatas
#2) verifica presença VIP
#3) relatorio

def limpar_inscritos_duplicados(emails: list) -> set:
    '''
    Recebe uma lista de Emails e retorna um set (Conjunto)
    param: lista de emails
    retorna: set com os emails
    '''
    return set(emails)

def verificar_presenca_vip(email: str, lista_limpa: set)-> bool:
    '''
    Verifica se um email está presente na presença vip 
    param: email e lista de emails(sem duplicatas)
    return: bool
    '''
    #logica Aqui...
    return email in lista_limpa

def analisar_frequencia(dia1:set, dia2:set)-> None:
    '''
    Aplica operações matemáticas de conjuntos para gerar relatorios
    param: set1, set2:set
    return: None
    '''
    #Union (|) - presente em pelo menos um set
    todos = dia1 | dia2 
    #todos = dia1.union(dia2)

    #intersection(&) - presente em ambos os sets
    frequentes = dia1 & dia2
    #freq = dia1.intersection(dia2)

    #Difenrence
    apenas_dia1 = dia1 - dia2
    #apenas_dia1 = dia1.diference(dia2)

    print("---Relatorio de Frenquencia---")
    print(f'Total Participantes: {len(todos)}')
    print(f'Participantes Assíduos: {frequentes}')
    print(f'Presentes no dia1: {apenas_dia1}')

#principal
email = [
    "ana@mail.com",
    "carlos@mail.com",
    "pedro@mail.com",
    "ana@mail.com",
    "maria@mail.com",
    "pedro@mail.com",
    "larissa@mail.com"
]    

inscritos_limpos = limpar_inscritos_duplicados(email)
print(f"Total de inscritos: {len(email)}")
print(f" inscrições validas: {len(inscritos_limpos)}")

email_vip = "larissa@mail.com"
if verificar_presenca_vip(email_vip, inscritos_limpos):
    print(f'{email_vip} esta na lista Vip')
else:
    print(f"{email_vip} Não esta na lista Vip")

print('----------')
presentes_dia1 ={"ana@mail.com", "pedro@mail.com", "carlos@mail.com"}
presentes_dia2 = {"ana@mail.com", "pedro@mail.com"}

analisar_frequencia(presentes_dia1, presentes_dia2)



