import numpy as np
import pandas as pd

bnList =list(range(8 ,29))
bpList =list(range(0 ,21))
bcList =list(range(3 ,12))

#针对人数
wnList =[0.1 ,0.2 ,0.3 ,0.4 ,0.5 ,0.6 ,0.7 ,0.8 ,0.9 ,1.0 ,1.1 ,1.2 ,1.3 ,1.4 ,1.5 ,1.6 ,1.7 ,1.8 ,1.9 ,2.0]
wpList =[0.1 ,0.2 ,0.3 ,0.4 ,0.5 ,0.6 ,0.7 ,0.8 ,0.9]
#针对48秒价差的差值
wcList =[0.1 ,0.2 ,0.3 ,0.4 ,0.5 ,0.6 ,0.7 ,0.8 ,0.9 ,1.0 ,1.1 ,1.2 ,1.3 ,1.4 ,1.5 ,1.6 ,1.7 ,1.8 ,1.9 ,2.0]

#一下所谓价格为最终价
#本次价格 =价格基准 +（这次人数-人数基准）*人差权重 +（上次价格基准blc -上次价格）*价格权重
# print(round(7 +(18 -20) *0.2 +(7 -4) *0.4))


data = pd.read_csv('../Datasets/chepai/48_17.csv')
tnList =data['tn1'].values
tpList =data['tp1'].values
lcList =data['lc'].values
tcList =data['tc'].values

# print((nn -27) *0.1)
# print((pp -2200) /100 *0.1)
# print((cc -300) /100 *0.5)

allList =[]

for bn in bnList:
    for blc in bcList:
        for bp in bpList:
            for wn in wnList:
                for wc in wcList:
                    absCount =0
                    theList =[]
                    count =0
                    countList =[]
                    count1 =0
                    countList1 =[]
                    for index in range(2 ,17):
                        theP =bp +(tnList[index] -bn) *wn +(blc -lcList[index]//100) *wc
                        absCount +=abs(theP -tpList[index])
                        theList.append(str(index)  +'-' +str(tpList[index]) +'-' +str(theP))
                        if round(theP) != tpList[index]:
                            count +=1
                            countList.append(index)
                        if round(theP) == tpList[index]:
                            if abs(theP -tpList[index]) >0.2:
                                count1 +=1
                                countList1.append(index)
                    allList.append([absCount ,count ,countList ,bn ,blc ,bp ,wn ,wc ,theList])


allList.sort(key=lambda col:(col[1] ,col[0]))
for index in range(101):
    print(allList[index])
    # if allList[index][3] ==3:
    #     print(allList[index])
    # if allList[index][4] ==allList[index][5]:
    #     print(allList[index])



# for bn in bnList :
#     for btc in bcList:
#         for wn in wnList:
#             count =0
#             countList =[]
#             absCount =0
#             theList =[]
#             for index in range(2 ,17):
#                 theC =btc +(tnList[index] -bn) *wn
#                 absCount +=abs(theC -tcList[index]//100)
#                 theList.append(str(index)  +'-' +str(tcList[index]//100) +'-' +str(theC))
#                 if round(theC) != tcList[index]//100:
#                     count +=1
#                     countList.append(index)
#             allList.append([absCount ,count ,countList ,bn ,btc ,wn ,theList])



