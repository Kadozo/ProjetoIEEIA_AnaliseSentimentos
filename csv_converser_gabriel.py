import csv

# abre o arquivo correspondente
file = open("comentarios_bruto.txt", 'r')
comentarios = file.readlines()

# csv writer criado
cw = csv.writer(open("comentarios.csv", "w"))

# escreve uma linha do csv para cada coluna
cw.writerow(["Avaliação"] + ["Comentário"])
for a in comentarios:
    linha = a.split(maxsplit=2)
    #remove o : da lista, pois não tem nenhuma utilidade para o csv.
    linha[1] = linha.pop(2)
    #separa toda a string da avaliação em uma lista, em que cada index é uma avaliação
    listAvalliation = linha[0].split(maxsplit=0)
    listAllComments = linha[1].split(maxsplit=0)
    #escreve em cada coluna do arquivo a sua avaliação e seu respectivo comentário.
    cw.writerow(listAvalliation + listAllComments)
