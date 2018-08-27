import numpy as np
import pandas as pd

#人数基准所在区间
llList =list(range(1 ,8))
#终价基准所在区间
ppList =list(range(1 ,24))
#采样区间价差基准所在区间
ccList =list(range(1 ,6))
#时间基准所在区间
ttList =[54.0 ,54.5 ,55.0 ,55.5 ,56.0]

w1List =[0 ,0.05 ,0.1 ,0.15 ,0.2]
w2List =[0 ,0.05 ,0.1 ,0.15 ,0.2 ,0.25 ,0.3]
w3List =[0.1 ,0.15 ,0.2 ,0.25 ,0.3 ,0.35 ,0.4 ,0.45 ,0.5]


#出价时间
data = pd.read_csv('../Datasets/chepai/theTime.csv')
nList =data['tn'].values
lList =data['lp'].values
pList =data['tp_54'].values
cList =data['49_54'].values
tList =data['tt'].values
tagList =data['tag1'].values


allList =[]
absList =[]

for ll in llList:
    for pp in ppList:
        for cc in ccList:
            for tt in ttList:
                for w1 in w1List:
                    for w2 in w2List:
                        for w3 in w3List:
                            absCount =0.0
                            theList =[]
                            count =0
                            for index in range(3 ,len(nList)):
                                if tagList[index] ==1:
                                    theT =tt +float(lList[index] -ll) *w1 +float(pp -pList[index]) *w2 +float(cc -cList[index]) *w3
                                    theT =round(theT ,2)
                                    theList.append(str(index)  +'-' +str(tList[index]) +'-' +str(theT))
                                    absCount +=abs(theT -float(tList[index]))
                                    if tList[index] >theT +0.5 or tList[index] <theT -0.5:
                                        count +=1
                                        countList.append(index)

                            absCount =round(absCount ,2)
                            if count <3 and zz <55.0:
                                allList.append([absCount ,count ,countList ,ll ,pp ,cc ,tt ,w1 ,w2 ,w3 ,theList])

allList.sort(key=lambda col:(col[1] ,col[0]))
for index in range(1001):
    print(allList[index])







# for index in range(len(nList)):
#     nList[index] =int(round(nList[index]/10000))
#     theT =54.5 +(nn -nList[index]) *0.1 +(pp -pList[index])/100 *0.1 +(cc -cList[index])/100 *0.5
#     print(str(index) +'---' +str(theT) +'---' +str(tList[index]) +'--:' +str(theT -tList[index]))