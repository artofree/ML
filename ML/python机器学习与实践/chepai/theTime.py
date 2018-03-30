import numpy as np
import pandas as pd

#人数基准所在区间
nnList =list(range(1 ,29))
#终价基准所在区间
ppList =list(range(1 ,24))
#采样区间价差基准所在区间
ccList =list(range(1 ,6))
#时间基准所在区间
ttList =[54.0 ,54.5 ,55.0 ,55.5 ,56.0]

w1List =[0 ,0.05 ,0.1]
w2List =[0.05 ,0.1 ,0.15]
w3List =[0.25 ,0.3 ,0.35 ,0.4 ,0.45]

#出价时间
# theList =['tn','tp','tc']
data = pd.read_csv('../Datasets/chepai/theTime.csv')
print(data)
nList =data['tn'].values
pList =data['tp_54'].values
cList =data['47_54'].values
tList =data['tt'].values

# print((nn -27) *0.1)
# print((pp -2200) /100 *0.1)
# print((cc -300) /100 *0.5)

#3-20采样的对于15和20最佳值：
# 18, 10, 2, 56, 0, 0.1, 0.3,[8 ,15]
#3-55.0-55.3', '4-54.5-54.7', '5-55.5-55.8', '6-55.5-55.5', '7-55.0-55.1', '8-56.5-55.9', '9-56.0-56.2', '10-54.5-55.0', '11-55.0-55.1', '12-56.0-55.6', '13-54.5-55.0', '14-54.0-54.1', '15-56.5-55.7', '16-56.0-55.7', '17-55.5-55.5', '18-56.5-56.1', '19-56.5-57.0', '20-55.5-55.8'
#18, 10, 2, 56.0, 0, 0.1, 0.45,[8, 15, 19]
#'3-55.0-55.3', '4-54.5-54.55', '5-55.5-55.95', '6-55.5-55.35', '7-55.0-54.8', '8-56.5-55.9', '9-56.0-56.35', '10-54.5-54.85', '11-55.0-54.8', '12-56.0-55.6', '13-54.5-54.85', '14-54.0-53.65', '15-56.5-55.7', '16-56.0-55.55', '17-55.5-55.35', '18-56.5-56.1', '19-56.5-57.3', '20-55.5-55.65'

allList =[]
absList =[]
sumList =[]

for nn in nnList:
    for pp in ppList:
        for cc in ccList:
            for tt in ttList:
                for w1 in w1List:
                    for w2 in w2List:
                        for w3 in w3List:
                            absCount =0.0
                            theList =[]
                            count =0
                            countList =[]
                            theSum =0.0
                            for index in range(3 ,len(nList)):
                                theT =tt +float(nn -nList[index]) *w1 +float(pp -pList[index]) *w2 +float(cc -cList[index]) *w3
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
                            if absCount not in absList or theSum not in sumList:
                                absList.append(absCount)
                                sumList.append(theSum)
                                allList.append([absCount ,count ,theSum ,countList ,nn ,pp ,cc ,tt ,w1 ,w2 ,w3 ,theList])

allList.sort(key=lambda col:(col[1] ,col[0]))
for index in range(101):
    print(allList[index])








# for index in range(len(nList)):
#     nList[index] =int(round(nList[index]/10000))
#     theT =54.5 +(nn -nList[index]) *0.1 +(pp -pList[index])/100 *0.1 +(cc -cList[index])/100 *0.5
#     print(str(index) +'---' +str(theT) +'---' +str(tList[index]) +'--:' +str(theT -tList[index]))