import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

df = pd.read_csv('comentarios.csv').sample(1000, random_state=42, replace=True)
comments = df["Comentário"]
evaluation = df["Avaliação"]
evaluation.value_counts()
df.head()

#vetorização dos dados
vect = CountVectorizer(ngram_range=(1, 1))
vect.fit(comments)
text_vect = vect.transform(comments)

#dados de treino e de teste
X_train,X_test,y_train,y_test = train_test_split(
    text_vect,  
    evaluation,
    test_size = 0.3, 
    random_state = 42
)

#Classe LogisticRegression - Modelo de machine learning
clf = LogisticRegression(random_state=0, solver='newton-cg')
clf = clf.fit(X_train, y_train)

#porcentagem de acerto do modelo
y_prediction = clf.predict(X_test)
f1 = f1_score(y_prediction, y_test, average='weighted')

print("porcentagem de acerto: ", f1)