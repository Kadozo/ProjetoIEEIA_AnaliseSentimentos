import nltk
import numpy as np
import pandas as pd
from nltk import word_tokenize
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

def writeResult(score, allBalanced, balancedFile, notBalancedFile): 
    if(allBalanced == True):
        balancedFile.write(str(score)+"\n")
    else:
        notBalancedFile.write(str(score)+"\n")
    
balancedFile = open("ResultadosBalanceadosNB.txt", "a")
notBalancedFile = open("ResultadosDesbalanceadosNB.txt", "a")
df = pd.read_csv("DB\\todos_commentarios.csv")

comments = df["Comentário"]
evaluation = df["Avaliação"]

#vetorização
tweet_tokenizer = TweetTokenizer()
vectorizer = CountVectorizer(analyzer="word", tokenizer = tweet_tokenizer.tokenize)
vect_comments = vectorizer.fit_transform(comments)

totalScore = 0
i=0
boole = False
allBalanced = False
resp = input("Deseja dados balanceados? y/n \n")
while(i < 10):
    while(boole == False):       
        if(resp == "y"):
            #pega todos os dados de forma balanceada
            
            boole = True
            allBalanced = True
        elif(resp == "n"):
            x_train, x_test, y_train, y_test = train_test_split(vect_comments, 
                                                                evaluation, 
                                                                test_size=0.3, 
                                                                random_state= np.random.randint(0,10000))
            boole = True
        else:
            boole = False

    #ML
    model= MultinomialNB()
    model.fit(x_train, y_train)


    #score
    prediction = model.predict(x_test)
    f1 = f1_score(prediction, y_test, average = 'weighted')

    print(f1)
    totalScore += f1
    i += 1   

    writeResult(f1, allBalanced, balancedFile, notBalancedFile)
    allBalanced = False
    boole = False

average = totalScore/10
balancedFile.close()
notBalancedFile.close()
print(average)
