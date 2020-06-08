import csv

# abre o arquivo correspondente
file = open("comentarios_bruto.txt", 'r')
file = file.readlines()

# csv writer criado
cw = csv.writer(open("comentarios.csv", "w"))

# escreve uma linha do csv
cw.writerow(["Avaliação", "Comentário"])

for a in file:
    linha = a.split(maxsplit=2)
    # os cochetes e aspas pra ficar apenas os comentários na string
    linha[2] = linha[2].replace('[', '')
    linha[2] = linha[2].replace(']', '')
    linha[2] = linha[2].replace('"', '')

    # escreve a avaliação e o comentário, respectivamente, numa linha do csv
    cw.writerow([linha[0], linha[2]])
