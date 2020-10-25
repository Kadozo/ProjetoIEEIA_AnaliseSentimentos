import pandas as pd
import random
#Essa funçao retorna um pands.DataFrame e com os comentarios balanceados pelo que tem menos entre recomendados e nao recomendados do comentarios.csv
def get_balanced():
    df = pd.read_csv("comentarios.csv")
    r=0
    n=0
    dfR = pd.DataFrame(columns=["Avaliação","Comentário"])
    dfN = pd.DataFrame(columns=["Avaliação","Comentário"])
    for a in range(df.last_valid_index()+1):
        if( df.loc[a]["Avaliação"] ==  "['R']"):
            dfR.at[r]=df.loc[a].values
            r+=1
        elif( df.loc[a]["Avaliação"] ==  "['N']"):
            dfN.at[n]=df.loc[a].values
            n+=1
        else:
            print(f'Erro at {a}')
    nwDF=pd.DataFrame(columns=["Avaliação","Comentário"])
    c=r
    if(r>n):
        c=n
    for a in range(c):
        nwDF.at[a] = dfR.loc[a].values
    for a in range(c):
        nwDF.at[a+c] = dfN.loc[a].values
    l=[]
    for a in range(nwDF.last_valid_index()+1):
        l.append(a)
    rDF = pd.DataFrame(columns=["Avaliação","Comentário"])
    c=0
    m = len(l)
    for a in range( m ):
        n = int(random.random()*10000000%len(l))
        rDF.at[c]=nwDF.loc[l[n]].values
        c+=1
        del(l[n])
    return rDF
#Essa funçao retorna um pands.DataFrame e com todos os comentarios do comentarios.csv colocados em ordem aleatoria
def shuffle():
    df = pd.read_csv("comentarios.csv")
    r=0
    n=0
    dfR = pd.DataFrame(columns=["Avaliação","Comentário"])
    dfN = pd.DataFrame(columns=["Avaliação","Comentário"])
    for a in range(df.last_valid_index()+1):
        if( df.loc[a]["Avaliação"] ==  "['R']"):
            dfR.at[r]=df.loc[a].values
            r+=1
        elif( df.loc[a]["Avaliação"] ==  "['N']"):
            dfN.at[n]=df.loc[a].values
            n+=1
        else:
            print(f'Erro at {a}')
    nwDF=pd.DataFrame(columns=["Avaliação","Comentário"])
    for a in range(r):
        nwDF.at[a] = dfR.loc[a].values
    for a in range(n):
        nwDF.at[a+r] = dfN.loc[a].values
    l=[]
    for a in range(nwDF.last_valid_index()+1):
        l.append(a)
    rDF = pd.DataFrame(columns=["Avaliação","Comentário"])
    c=0
    m = len(l)
    for a in range( m ):
        n = int(random.random()*10000000%len(l))
        rDF.at[c]=nwDF.loc[l[n]].values
        c+=1
        del(l[n])
    return rDF
