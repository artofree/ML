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

w1List =[0 ,0.05 ,0.1 ,0.15 ,0.2 ,0.25 ,0.3]
w2List =[0 ,0.05 ,0.1 ,0.15 ,0.2 ,0.25 ,0.3 ,0.35 ,0.4 ,0.45 ,0.5]

#49最优：
#[3.1, 0, [], 13, 3, 55.0, 0.05, 0.2, ['3-55.0-55.0', '4-54.5-54.6', '5-55.5-55.05', '6-55.5-55.45', '7-55.0-54.75', '10-54.5-54.75', '11-55.0-54.75', '13-54.5-54.75', '14-54.0-54.2', '16-56.0-55.55', '17-55.5-55.25', '20-55.2-55.35', '22-54.5-54.55', '23-55.0-54.6']]

#48最优：
#



#出价时间
data = pd.read_csv('../Datasets/chepai/theTime.csv')
nList =data['tn'].values
lList =data['lp'].values
pList =data['tp_54'].values
cList =data['47_54'].values
tList =data['tt'].values
tagList =data['tag1'].values

#49:
#[0.3, 0, [], 1, 1, 55.5, 0, 0.25, ['3-55.0-55.25', '4-54.5-55.0', '5-55.5-55.25', '6-55.5-55.5', '7-55.0-54.75', '10-54.5-55.0', '11-54.5-54.75', '13-54.5-55.0', '14-54.0-54.5', '16-55.5-55.5', '17-55.0-55.25', '20-55.2-55.25', '22-54.5-54.5', '23-55.0-55.0']]
#48:
#[0.45, 0, [], 1, 1, 55.5, 0, 0.25, ['3-55.0-55.25', '4-54.5-54.75', '5-55.5-55.25', '6-55.5-55.5', '7-55.0-54.75', '10-54.5-55.0', '11-54.5-54.5', '13-54.5-55.0', '14-54.0-54.5', '16-55.5-55.5', '17-55.0-55.0', '20-55.2-55.0', '22-54.5-54.5', '23-55.0-54.75']]



allList =[]
absList =[]

for pp in ppList:
    for cc in ccList:
        for tt in ttList:
            for w1 in w1List:
                for w2 in w2List:
                    absCount =0.0
                    theList =[]
                    count =0
                    countList =[]
                    for index in range(3 ,len(nList)):
                        if tagList[index] ==1:
                            theT =tt +float(pp -pList[index]) *w1 +float(cc -cList[index]) *w2
                            theT =round(theT ,2)
                            theList.append(str(index)  +'-' +str(tList[index]) +'-' +str(theT))
                            if index >15:
                                absCount +=abs(theT -float(tList[index]))
                            if tList[index] >theT +0.5 or tList[index] <theT -0.5:
                                count +=1
                                countList.append(index)

                    absCount =round(absCount ,2)
                    if count <3:
                        allList.append([absCount ,count ,countList ,pp ,cc ,tt ,w1 ,w2 ,theList])

allList.sort(key=lambda col:(col[1] ,col[0]))
for index in range(len(allList)):
    print(allList[index])







# for index in range(len(nList)):
#     nList[index] =int(round(nList[index]/10000))
#     theT =54.5 +(nn -nList[index]) *0.1 +(pp -pList[index])/100 *0.1 +(cc -cList[index])/100 *0.5
#     print(str(index) +'---' +str(theT) +'---' +str(tList[index]) +'--:' +str(theT -tList[index]))