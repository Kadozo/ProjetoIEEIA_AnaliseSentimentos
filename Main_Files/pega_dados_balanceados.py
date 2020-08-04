import pandas as pd
import random
def get_dados(df,sample_size=0.8,balanced=True):
    coment=df["Comentário"]
    aval = df["Avaliação"]
    cR = []
    cN = []
    for a in range(len(aval)):
        if( aval[a] ==  "['R']"):
            cR.append(coment[a])
        elif( aval[a] ==  "['N']"):
            cN.append(coment[a])
        else:
            print(f'Erro at {a}')
    r = len(cR)
    n = len(cN)
    treino = get_df(cR[:int(r*sample_size)],cN[:int(n*sample_size)],balanced)
    test   = get_df(cR[int(r*sample_size):],cN[int(n*sample_size):],balanced)
    
    
    return embaralhar(treino),embaralhar(test)

def embaralhar(nwDF):
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

def get_df(vR,vN,balanced):
    nwDF=pd.DataFrame(columns=["Avaliação","Comentário"])
    c=len(vR)
    if( balanced == True and len(vR)>len(vN)):    
        c=len(vN)
    for a in range(c):
        nwDF.at[a] = {"Avaliação":"['R']","Comentário":vR[a]}
    c2=len(vN)
    if( balanced == True and len(vN)>len(vR)):    
        c2=len(vR)
    for a in range(c2):
        nwDF.at[a+c] = {"Avaliação":"['N']","Comentário":vN[a]}
    return nwDF
