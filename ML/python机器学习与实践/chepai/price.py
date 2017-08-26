import numpy as np
import pandas as pd

#lc:上月最终价比45秒价格差
#45p:45秒的价格
#n:人数
#w:额度数
#p:最终价
# theList =['t45p','tn','tw']
# theList =['ll45p','lln','llw','llc','l45p','ln','lw','lc','t45p','tn','tw']
# theList =['ll45p','lln','llc','l45p','ln','lc','t45p','tn']
# theList =['ll45p','lln','l45p','ln','t45p','tn']
# theList =['l45p','ln','lc','t45p','tn']
theList =['ln','lc','tn']
# theList =['lln','llc','ln','lc','tn']
# theList =['llc','lc']
# theList =['lc','t45p','tn','tw']
# theList =['lc']

data = pd.read_csv('../Datasets/chepai/48_17.csv')
# print(data)
# print('-------')
priceList =[]

for index in range(0 ,17):
    iList =list(range(0 ,17))
    iList.remove(index)

    X_train =data.loc[iList ,theList]
    # print('xtrain:')
    # print(X_train)
    # print('-------')
    # print(X_train.drop('lc' ,axis =1))
    y_train =data.loc[iList ,'tc']
    # print('ytrain:')
    # print(y_train)
    # print('-------')
    X_test =data.loc[[index] ,theList]
    # print('x_test:')
    # print(X_test)

    ###分类
    # from sklearn.svm import LinearSVC
    # ml = LinearSVC()

    # from sklearn.linear_model import LogisticRegression
    # ml = LogisticRegression()

    ###回归
    # from sklearn.linear_model import LinearRegression
    # ml = LinearRegression()

    # from sklearn.svm import SVR
    # ml = SVR(kernel='linear')
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
    ml =RandomForestRegressor()

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
    print(str(index) +'---' +str(y_predict[0]))