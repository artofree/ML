import numpy as np
import pandas as pd

#出价时间
# theList =['tn','53p','50c']
theList =['tn']
# theList =['53p','50c']
# theList =['50c']

# data = pd.read_csv('../Datasets/chepai/48_17.csv')
data = pd.read_csv('../Datasets/chepai/time_53.csv')
# print(data)
# print('-------')
priceList =[]

#估计正确统计和
correctCount =0
for index in range(0 ,17):
    iList =list(range(0 ,17))
    iList.remove(index)

    X_train =data.loc[iList ,theList]
    # print('xtrain:')
    # print(X_train)
    # print('-------')

    y_train =data.loc[iList ,'tt']
    # print('ytrain:')
    # print(y_train)
    # print('-------')
    X_test =data.loc[[index] ,theList]
    # print('x_test:')
    # print(X_test)
    # print('-------')
    y_test =data.loc[[index] ,'tt']

    ###分类
    from sklearn.svm import LinearSVC
    # ml = LinearSVC()

    from sklearn.linear_model import LogisticRegression
    # ml = LogisticRegression()

    ###回归
    from sklearn.linear_model import LinearRegression
    # ml = LinearRegression()

    from sklearn.svm import SVR
    ml = SVR(kernel='linear')
    # ml = SVR(kernel='poly')
    # ml = SVR(kernel='rbf')

    #树与森林
    from sklearn.tree import DecisionTreeClassifier
    # ml =DecisionTreeClassifier()

    from sklearn.ensemble import RandomForestClassifier
    # ml =RandomForestClassifier()

    from sklearn.ensemble import GradientBoostingClassifier
    # ml =GradientBoostingClassifier()

    #树与森林回归
    from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor
    # ml =GradientBoostingRegressor()
    # ml =ExtraTreesRegressor()
    # ml =RandomForestRegressor()

    #xgboost
    from xgboost import XGBRegressor
    # ml =XGBRegressor()

    #如果用树与森林，则不要标准化?
    from sklearn.preprocessing import StandardScaler
    ss_X = StandardScaler()
    # ss_y = StandardScaler()
    X_train = ss_X.fit_transform(X_train)
    X_test = ss_X.transform(X_test)
    # y_train = ss_y.fit_transform(y_train)
    # y_test = ss_y.transform(y_test)

    ml.fit(X_train, y_train)
    y_predict = ml.predict(X_test)
    # priceList.append(y_predict[0])
    result ='0'
    if y_test.values[0] >y_predict[0] -0.5 and y_test.values[0] <y_predict[0] +0.5:
        result ='1'
        correctCount +=1
    print(str(index) +'---' +str(y_predict[0]) +'---' +str(y_test.values[0]) +'---' +result)

print(correctCount)
