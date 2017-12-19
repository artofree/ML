import numpy as np
import pandas as pd

bnList =list(range(0 ,29))
bpList =list(range(0 ,2100 ,100))
bcList =list(range(0 ,15))

#48最佳：
#[6.8500000000000005, 4, 3, [7, 9, 13], 1, [12], 23, 7, 7, 0.3, 0.25, ['2-7-7.1', '3-7-6.7', '4-8-7.9', '5-8-8.25', '6-8-8.05', '7-8-7.35', '8-7-6.75', '9-9-7.45', '10-6-6.2', '11-7-7.25', '12-8-7.6', '13-10-7.65', '14-7-6.85', '15-8-8.2', '16-9-8.95']]
#46最佳：
#[7.9999999999999982, 4, 1, [9], 3, [5, 7, 12], 23, 8, 8, 0.3, 0.2, ['2-8-7.9', '3-8-7.7', '4-9-8.9', '5-9-9.3', '6-9-9.1', '7-9-8.4', '8-9-7.8', '9-10-8.3', '10-7-7.3', '11-8-8.2', '12-9-8.6', '13-10-8.7', '14-8-8.2', '15-9-9.2', '16-11-10.0']]
#[7.8999999999999986, 6, 1, [9], 5, [3, 7, 8, 12, 13], 15, 6, 6, 0.3, 0.25, ['2-8-8.0', '3-8-7.6', '4-9-8.8', '5-9-9.15', '6-9-9.2', '7-9-8.25', '8-9-7.65', '9-10-8.35', '10-7-7.1', '11-8-8.15', '12-9-8.5', '13-10-8.55', '14-8-8.0', '15-9-9.1', '16-11-10.1']]
#46，l48c最佳：
#[7.9999999999999973, 6, 1, [9], 5, [3, 7, 8, 12, 13], 24, 8, 8, 0.3, 0.25, ['2-8-8.05', '3-8-7.65', '4-9-8.85', '5-9-9.2', '6-9-9.0', '7-9-8.3', '8-9-7.7', '9-10-8.4', '10-7-7.15', '11-8-8.2', '12-9-8.55', '13-10-8.6', '14-8-7.8', '15-9-9.15', '16-11-9.9']]

#lc:上月最终价比45秒价格差
#45p:45秒的价格
#n:人数
#w:额度数
#p:最终价

#针对人数
wnList =[0.1 ,0.2 ,0.3 ,0.4 ,0.5]
wpList =[0.1 ,0.2 ,0.3 ,0.4 ,0.5 ,0.6 ,0.7 ,0.8 ,0.9]
#针对48秒价差的差值
wcList =[0.1 ,0.15 ,0.2 ,0.25 ,0.3 ,0.35 ,0.4 ,0.45 ,0.5]

#一下所谓价格为46秒增量
#bn ,blc ,btc ,wn ,wc
#本次价格 =价格基准 +（这次人数-人数基准）*人差权重 +（上次价格基准 -上次价格）*价差权重
#theC   =btc     +(tnList[index] -bn) *wn  +(blc -lcList[index]//100) *wc
# print(round(7 +(18 -20) *0.2 +(7 -4) *0.4))


data = pd.read_csv('../Datasets/chepai/46_17.csv')
tnList =data['tn1'].values
tpList =data['tp'].values
lcList =data['l48c'].values
# lcList =data['lc'].values
tcList =data['tc'].values

# print((nn -27) *0.1)
# print((pp -2200) /100 *0.1)
# print((cc -300) /100 *0.5)

allList =[]

for bn in bnList:
    for blc in bcList:
        for btc in bcList:
            for wn in wcList:
                for wc in wcList:
                    absCount =0
                    theList =[]
                    count =0
                    countList =[]
                    count1 =0
                    countList1 =[]
                    allCount =0
                    for index in range(2 ,18):
                        theC =btc +(tnList[index] -bn) *wn +(blc -lcList[index]//100) *wc
                        absCount +=abs(theC -tcList[index]//100)
                        theList.append(str(index)  +'-' +str(tcList[index]//100) +'-' +str(theC))
                        if round(theC) != tcList[index]//100 and round(theC) != tcList[index]//100 -1:
                            allCount +=1
                            count +=1
                            countList.append(index)
                        if round(theC) == tcList[index]//100:
                            if abs(theC -tcList[index]//100) >0.2:
                                allCount +=1
                                count1 +=1
                                countList1.append(index)
                        if round(theC) +1 == tcList[index]//100:
                            if abs(theC +1 -tcList[index]//100) >0.2:
                                allCount +=1
                                count1 +=1
                                countList1.append(index)
                    allList.append([absCount ,allCount ,count ,countList ,count1 ,countList1 ,bn ,blc ,btc ,wn ,wc ,theList])


allList.sort(key=lambda col:(col[1] ,col[2] ,col[0]))
for index in range(1001):
    print(allList[index])
    # if allList[index][1] ==6 and allList[index][2] ==1:
    #     print(allList[index][8] +(27 -allList[index][6]) *allList[index][9] +(allList[index][7] -9) *allList[index][10])
    # if allList[index][1] ==4 and allList[index][2] ==3:
    #     print(allList[index][8] +(27 -allList[index][6]) *allList[index][9] +(allList[index][7] -9) *allList[index][10])

    # if allList[index][3] ==3:
    #     print(allList[index])
    # if allList[index][8] ==allList[index][7]:
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



