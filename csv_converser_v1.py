import csv
import nltk as nk
# abre o arquivo correspondente
file = open("comentarios_bruto.txt", "r")


# csv writer criado
cw = csv.writer(open('comentarios.csv', 'w', newline=''), delimiter=' ')

# escreve uma linha do csv para cada coluna
cw.writerow(["Avaliação"] + ["Comentário"])
linha = linha = file.readline()
linhaSep = [" "]
while(linha != ""):  
    linhaSep = linha.split(maxsplit=2)
      
    #remove o : da lista, pois não tem nenhuma utilidade para o csv.
    linhaSep[1] = linhaSep.pop(2)
    
    #separa toda a string da avaliação em uma lista, em que cada index é uma avaliação
    Avalliation = linhaSep[0].split(maxsplit=0)
    Comment = linhaSep[1].split(maxsplit=0)
    Comment = Comment[0].replace("[", "")
    Comment = Comment.replace("]", "")
    Comment = Comment.replace(".", "")
    CommentToken = nk.word_tokenize(Comment)
    #escreve em cada coluna do arquivo a sua avaliação e seu respectivo comentário.
    cw.writerow(Avalliation + CommentToken)
    print(Avalliation + CommentToken)
    linha = file.readline()
print("Os comentários foram tokenizados e importados para um arquivo .csv!")