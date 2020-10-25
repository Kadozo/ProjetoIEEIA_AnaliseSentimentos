import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import pickle
import numpy as np
df = pd.read_csv("DB\\todos_commentarios.csv")
i = 0
y = []
while i<df.shape[0]:
    y.append(df.loc[i,'Avaliação'])
    i = i+1
x = []
i = 0
while i<df.shape[0]:
    x.append(df.loc[i,'Comentário'])
    i = i+1

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = np.random.randint(0,10000))
pipe = Pipeline([('counts', CountVectorizer()),('classifier', SVC(kernel='linear',probability=True,random_state = np.random.randint(0,10000)))])
pipe.fit(x_train,y_train)
print(pipe.score(x_test,y_test))

#Salvando o Modelo
pickle.dump(pipe, open("models\\SVM.sav", 'wb'))