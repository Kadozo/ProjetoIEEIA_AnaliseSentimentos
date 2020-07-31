import pandas as pd
import nltk
import balancear
import random
from nltk import word_tokenize
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#pego todos os dados de forma balanceada 50%-50%
dados = balancear.get_balanced()
coment=dados["Comentário"]
aval = dados["Avaliação"]

#dados de treino
dados_treino = coment[:int(len(coment) *.8) ]
dados_treino_aval = aval[:int(len(aval) *.8) ]

#dados de teste
dados_test = coment[int(len(coment) *.8): ]
dados_test_aval = aval[int(len(aval) *.8): ]

#vetorização
tweet_tokenizer = TweetTokenizer()
vectorizer = CountVectorizer(analyzer="word", tokenizer = tweet_tokenizer.tokenize)
freq_comments = vectorizer.fit_transform(dados_treino)

#ML
modelLearn= MultinomialNB()
modelLearn.fit(freq_comments, dados_treino_aval)

#print dos predicts pra cada comentário
freq_comments = vectorizer.transform(dados_test)
for t, c in zip (dados_test, modelLearn.predict(freq_comments)):
    print(t + ", " + c)

#array de probabilidades
print(modelLearn.classes_)
print(modelLearn.predict_proba(freq_comments).round(2))

#score
print(modelLearn.score(freq_comments, dados_test_aval))
