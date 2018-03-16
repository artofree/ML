import numpy as np
import pandas as pd

#人数基准所在区间
nnList =list(range(18 ,29))
#终价基准所在区间
ppList =list(range(10 ,24))
#采样区间价差基准所在区间
ccList =list(range(1 ,6))
#时间基准所在区间
ttList =[54 ,54.5 ,55 ,55.5 ,56]

w1List =[0 ,0.05 ,0.1]
w2List =[0.05 ,0.1 ,0.15]
w3List =[0.25 ,0.3 ,0.35 ,0.4 ,0.45]

#出价时间
# theList =['tn','tp','tc']
data = pd.read_csv('../Datasets/chepai/theTime.csv')
nList =data['tn'].values
pList =data['tp_53'].values
cList =data['47_53'].values
tList =data['tt'].values

# print((nn -27) *0.1)
# print((pp -2200) /100 *0.1)
# print((cc -300) /100 *0.5)

#最佳值：18, 20, 4, 55, 0.1, 0.1, 0.3

allList =[]

for nn in nnList:
    for pp in ppList:
        for cc in ccList:
            for tt in ttList:
                for w1 in w1List:
                    for w2 in w2List:
                        for w3 in w3List:
                            absCount =0
                            theList =[]
                            count =0
                            countList =[]
                            for index in range(3 ,len(nList)):
                                theT =tt +(nn -nList[index]) *w1 +(pp -pList[index]) *w2 +(cc -cList[index]) *w3
                                theList.append(str(index)  +'-' +str(tList[index]) +'-' +str(theT))
                                absCount +=abs(theT -tList[index])
                                if tList[index] >theT +0.5 or tList[index] <theT -0.5:
                                    count +=1
                                    countList.append(index)
                            allList.append([absCount ,count ,countList ,nn ,pp ,cc ,tt ,w1 ,w2 ,w3 ,theList])

allList.sort(key=lambda col:(col[0] ,col[1]))
for index in range(1001):
    print(allList[index])








# for index in range(len(nList)):
#     nList[index] =int(round(nList[index]/10000))
#     theT =54.5 +(nn -nList[index]) *0.1 +(pp -pList[index])/100 *0.1 +(cc -cList[index])/100 *0.5
#     print(str(index) +'---' +str(theT) +'---' +str(tList[index]) +'--:' +str(theT -tList[index]))