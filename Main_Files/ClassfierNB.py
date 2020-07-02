import pandas as pd
import nltk
from nltk import word_tokenize
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

file = pd.read_csv('comentarios.csv')

comments = file["Comentário"]
avaliation = file["Avaliação"]

tweet_tokenizer = TweetTokenizer()
vectorizer = CountVectorizer(analyzer="word", tokenizer = tweet_tokenizer.tokenize)
freq_comments = vectorizer.fit_transform(comments)
modelLearn= MultinomialNB()
modelLearn.fit(freq_comments, avaliation)

testes = ['O sistema de montarias é fabuloso!',
          'Incrível o realismo desse game.',
          'Dofus é simplesmente amor, que jogo sensacional!',
          'Que droga de jogo, quem criou isso merece um castigo',
          'Da pro gasto',
          'Não gostei.',
          'Está no começo do jogo, vamos ver se as atualizações irão melhorá-lo']

freq_comments = vectorizer.transform(testes)
for t, c in zip (testes, modelLearn.predict(freq_comments)):
    print(t + ", " + c)



#print(modelLearn.predict_proba(freq_comments).round(2))


