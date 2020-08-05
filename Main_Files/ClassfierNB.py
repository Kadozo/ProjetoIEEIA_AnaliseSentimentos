import nltk
import pandas as pd
import pega_dados_balanceados
from nltk import word_tokenize
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def writeResult(score, allBalanced, balancedFile, notBalancedFile): 
    if(allBalanced == True):
        balancedFile.write(str(score)+"\n")
    else:
        notBalancedFile.write(str(score)+"\n")
    
balancedFile = open("ResultadosBalanceadosNB.txt", "w")
notBalancedFile = open("ResultadosDesbalanceadosNB.txt", "w")
totalScore = 0
i=0
boole = False
allBalanced = False
resp = input("Deseja dados balanceados? y/n \n")
while(i < 10):
    while(boole == False):       
        if(resp == "y"):
            #pego todos os dados de forma balanceada 50%-50%
            dados_treino, dados_test = pega_dados_balanceados.get_dados(pd.read_csv("comentarios.csv"), balanced = True)
            boole = True
            allBalanced = True
        elif(resp == "n"):
            #pega os dados desbalanceados
            dados_treino, dados_test = pega_dados_balanceados.get_dados(pd.read_csv("comentarios.csv"), balanced = False)
            boole = True
        else:
            boole = False
              
    #dados de treino
    comment_train = dados_treino["Comentário"]
    aval_train = dados_treino["Avaliação"]

    #dados de teste
    comment_test = dados_test["Comentário"]
    aval_test = dados_test["Avaliação"]

    #vetorização
    tweet_tokenizer = TweetTokenizer()
    vectorizer = CountVectorizer(analyzer="word", tokenizer = tweet_tokenizer.tokenize)
    freq_comments = vectorizer.fit_transform(comment_train)

    #ML
    modelLearn= MultinomialNB()
    modelLearn.fit(freq_comments, aval_train)

    freq_comments = vectorizer.transform(comment_test)

    #score
    score = modelLearn.score(freq_comments, aval_test)
    print(score)
    totalScore += score
    i += 1   
    writeResult(score, allBalanced, balancedFile, notBalancedFile)
    allBalanced = False
    boole = False

average = totalScore/10
balancedFile.close()
notBalancedFile.close()
print(average)
