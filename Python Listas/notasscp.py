def calcular_media_checkpoints(notas_cp):
    menor_nota = notas_cp[0]
    soma_total = 0

    for nota in notas_cp:
        if nota < menor_nota:
            menor_nota = nota

        soma_total += nota

    soma_total_validas = soma_total - menor_nota
    media = soma_total_validas / 2

    return media


def calcular_media_sprits(notas_sprint):
    soma = 0

    for nota in notas_sprint:
        soma += nota

    media = soma / 2

    return media


def calcular_media_semestre(notas_cp, notas_sprint, nota_gs):
    media_cp = calcular_media_checkpoints(notas_cp)
    media_sprint = calcular_media_sprits(notas_sprint)

    nota_semestre = (media_cp * 0.20) + (media_sprint * 0.20) + (nota_gs * 0.60)

    return nota_semestre


cps_semestre1 = [7.0, 7.0, 10.0]
sprints_semestre1 = [8.0, 10.0]
gs_semestre1 = 7.0

nota_semestre1 = calcular_media_semestre(
    cps_semestre1,
    sprints_semestre1,
    gs_semestre1
)


cps_semestre2 = [6.0, 8.0, 10.0]
sprints_semestre2 = [7.0, 9.0]
gs_semestre2 = 8.5

nota_semestre2 = calcular_media_semestre(
    cps_semestre2,
    sprints_semestre2,
    gs_semestre2
)


media_final = (nota_semestre1 * 0.40) + (nota_semestre2 * 0.60)

print("Nota do semestre 1:", nota_semestre1)
print("Nota do semestre 2:", nota_semestre2)
print("Média final:", media_final)