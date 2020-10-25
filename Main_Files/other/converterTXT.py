import pandas as pd
import re
import nltk as nk


# ----------- Inicio da Declaração de funções ---------------

# Recebe uma lista de token e retorna uma lista de token sem stopwords
def remove_stopwords(tokens):
    # Pega a lista de stopwords da biblioteca nltk
    stopwords = set(nk.corpus.stopwords.words('english'))
    frase_tratada = []
    # Qualquer palavra que não esteja na lista de stopwords é adicionada em frase_tratada
    for palavra in tokens:
        if palavra not in stopwords:
            frase_tratada.append(palavra)
    return frase_tratada


# Recebe uma lista de tokens e retorna uma lista de tokens sem os caracteres especificados
def remove_caracter(tokens):
    token_tratado = []
    for word in tokens:
        word = re.sub('[.:;,+-=_!@#$?*()<>~^/|\'"]', '', word)
        token_tratado.append(word)
    for w in token_tratado:
        if w == '':
            token_tratado.remove(w)
    return token_tratado


# Função para remover os emojis do texto by: https://stackoverflow.com/a/49146722/330558 &
# https://www.reddit.com/r/learnpython/comments/8br5sz/removing_emojis_from_words_python3/dx91wrm/
def remove_emoji(string):
    emoji_pattern = re.compile("["
                               "\U0001F600-\U0001F64F"  # emoticons
                               "\U0001F300-\U0001F5FF"  # symbols & pictographs
                               "\U0001F680-\U0001F6FF"  # transport & map symbols
                               "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "\U00002702-\U000027B0"
                               "\U000024C2-\U0001F251"
                               "\U00010000-\U0010ffff"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


# ----------- Inicio da Declaração de funções ---------------

# abre o arquivo correspondente
file = open("todos_commentarios.txt", "r", encoding="UTF-8")
# cria um pandas.DataFrame para armazena os resultados
df = pd.DataFrame(columns=["Avaliação", "Comentário"])
linha = file.readline()
while linha != "":
    linhaSep = linha.split(",", maxsplit=1)
    # separa toda a string da avaliação em uma lista, em que cada index é uma avaliação
    Avalliation = linhaSep[0]
    Comment = linhaSep[1]
    Tokenizer = nk.TweetTokenizer(reduce_len=3)
    Comment = remove_emoji(Comment)
    Comment = Tokenizer.tokenize(Comment)
    Comment = remove_stopwords(Comment)
    Comment = remove_caracter(Comment)
    # escreve em cada coluna do arquivo a sua avaliação e seu respectivo comentário.
    df = df.append({"Avaliação": Avalliation, "Comentário": Comment}, ignore_index=True)
    linha = file.readline()  # manuntenção do loop

df.to_csv("todos_commentarios.csv", index=False)  # salvando o csv
