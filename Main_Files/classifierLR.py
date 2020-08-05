import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
import pega_dados_balanceados

#balanceamento
def writeResult(score, allBalanced, balancedFile, notBalancedFile): 
    if(allBalanced == True):
        balancedFile.write(str(score)+"\n")
    else:
        notBalancedFile.write(str(score)+"\n")
    
balancedFile = open("ResultadosBalanceadosLR.txt", "a")
notBalancedFile = open("ResultadosDesbalanceadosLR.txt", "a")
totalScore = 0
i=0
allBalanced = False
resp = input("Deseja dados balanceados? y/n \n")
while ( i < 10):
    if(resp ==  "y"):
        #pego todos os dados de forma balanceada 50%-50%
        dtr,dts = pega_dados_balanceados.get_dados(pd.read_csv("comentarios.csv"),balanced = True)
        allBalanced = True
    elif(resp == "n"):
        #pega os dados desbalanceados
        dtr,dts = pega_dados_balanceados.get_dados(pd.read_csv("comentarios.csv"),balanced = False)

    #df = pd.read_csv('comentarios.csv').sample(1000, random_state=42, replace=True)
    for c in dts.values:
        dtr.at[ dtr.last_valid_index()+1] = c


    comments = dtr["Comentário"]
    evaluation = dtr["Avaliação"]
    evaluation.value_counts()

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

    # score
    totalScore += f1
    i += 1   
    writeResult(f1, allBalanced, balancedFile, notBalancedFile)
    allBalanced = False

average = totalScore/10
balancedFile.close()
notBalancedFile.close()
print(average)
