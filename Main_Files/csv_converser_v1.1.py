import pandas as pd
import nltk as nk
import re


# Recebe uma lista de token e retorna uma lista de token sem stopwords
def remove_stopwords(tokens):
    # Pega a lista de stopwords da biblioteca nltk
    stopwords = set(nk.corpus.stopwords.words('portuguese'))
    frase_tratada = []
    # Qualquer palavra que não esteja na lista de stopwords é adicioinada em frase_tratada
    for palavra in tokens:
        if palavra not in stopwords:
            frase_tratada.append(palavra)
    return frase_tratada


# Recebe uma lista de tokens e retorna uma lista de tokens sem os caracteres especificados
def remove_caracter(tokens):
    token_tratado = []
    for word in tokens:
        word = re.sub('[.:;.,!@#$"''"]', '', word)
        token_tratado.append(word)
    for w in token_tratado:
        if w == '':
            token_tratado.remove(w)
    return token_tratado


# abre o arquivo correspondente
file = open("comentarios_bruto.txt", "r")

# cria um pandas.DataFrame para armazena os resultados
df = pd.DataFrame(columns=["Avaliação", "Comentário"])


linha = file.readline()
while linha != "":
    linhaSep = linha.split(maxsplit=2)

    # remove o : da lista, pois não tem nenhuma utilidade para o csv.
    linhaSep[1] = linhaSep.pop(2)

    # separa toda a string da avaliação em uma lista, em que cada index é uma avaliação
    Avalliation = linhaSep[0].split(maxsplit=0)
    Comment = linhaSep[1].split(maxsplit=0)

    Comment = Comment[0].replace("[", "")
    Comment = Comment.replace("]", "")
    Comment = Comment.replace(".", "")

    Tokenizer = nk.TweetTokenizer(reduce_len=3)
    Comment = Tokenizer.tokenize(Comment)
    Comment = remove_stopwords(Comment)
    CommentToken = remove_caracter(Comment)
    # escreve em cada coluna do arquivo a sua avaliação e seu respectivo comentário.
    df = df.append({"Avaliação":Avalliation,"Comentário":Comment}, ignore_index=True)

    linha = file.readline()

print(df)
df.to_csv("comentarios.csv", index=False)
print("Os comentários foram tokenizados e importados para um arquivo .csv!")