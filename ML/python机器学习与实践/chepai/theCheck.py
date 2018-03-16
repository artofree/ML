import numpy as np
import pandas as pd


data = pd.read_csv('../Datasets/chepai/theTime.csv')
nList =data['tn'].values
pList =data['tp_53'].values
cList =data['50_53'].values
tList =data['tt'].values

def theFun():
    absCount =0.0
    theList =[]
    count =0
    countList =[]
    theSum =0.0
    for index in range(3 ,len(nList)):
        theT =tb +float(nb -nList[index]) *nw +float(pb -pList[index]) *pw +float(cb -cList[index]) *cw
        theT =round(theT ,2)
        theList.append(str(index)  +'-' +str(tList[index]) +'-' +str(theT))
        absCount +=abs(theT -float(tList[index]))
        if tList[index] >theT +0.5 or tList[index] <theT -0.5:
            count +=1
            countList.append(index)
        if index ==15:
            theSum +=abs(theT -float(tList[index]))
        if index ==20:
            theSum +=abs(theT -float(tList[index]))

    absCount =round(absCount ,2)
    theSum =round(theSum ,2)
    print([absCount ,count ,theSum ,countList ,theList])

nb ,pb ,cb ,tb ,nw ,pw ,cw =22, 17, 2, 55, 0.1, 0.1, 0.5
# theFun()
cList =data['47_53'].values
nb ,pb ,cb ,tb ,nw ,pw ,cw =18, 10, 2, 56, 0, 0.1, 0.3
theFun()
cList =data['47_53'].values
nb ,pb ,cb ,tb ,nw ,pw ,cw =18, 10, 2, 56.0, 0, 0.1, 0.45
# theFun()