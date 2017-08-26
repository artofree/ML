# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

df_train = pd.read_csv('../Datasets/Breast-Cancer/breast-cancer-train.csv')
df_test = pd.read_csv('../Datasets/Breast-Cancer/breast-cancer-test.csv')
# print(df_test)

#选取两个特征是为了可以图例化
#也展示了关键特征为部分特征这个问题
df_test_negative = df_test.loc[df_test['Type'] == 0][['Clump Thickness', 'Cell Size']]
df_test_positive = df_test.loc[df_test['Type'] == 1][['Clump Thickness', 'Cell Size']]
test =df_test.loc[df_test['Type'] == 1]
print(test)
print(test.loc[10:20 ,['Clump Thickness', 'Cell Size']])

# negT =plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'], marker = 'o', c='red')
# posT =plt.scatter(df_test_positive['Clump Thickness'],df_test_positive['Cell Size'], marker = 'x', c='black')
# plt.xlabel('Clump Thickness')
# plt.ylabel('Cell Size')
# plt.show()

# intercept = np.random.random([1.csv])
# coef = np.random.random([2])
# lx = np.arange(0, 15)
# ly = (-intercept - lx * coef[0]) / coef[1.csv]
# plt.plot(lx, ly, c='yellow')
# plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'], marker = 'o', s=200, c='red')
# plt.scatter(df_test_positive['Clump Thickness'],df_test_positive['Cell Size'], marker = 'x', s=150, c='black')
# plt.xlabel('Clump Thickness')
# plt.ylabel('Cell Size')
# plt.show()

lr = LogisticRegression()
# lr.fit(df_train[['Clump Thickness', 'Cell Size']][:10], df_train['Type'][:10])
# print(df_train[['Clump Thickness', 'Cell Size']])
# print(df_train['Type'])
lr.fit(df_train[['Clump Thickness', 'Cell Size']], df_train['Type'])
print('Testing accuracy (10 training samples):', lr.score(df_test[['Clump Thickness', 'Cell Size']], df_test['Type']))
intercept = lr.intercept_
coef = lr.coef_[0, :]
lx = np.arange(0, 15)
ly = (-intercept - lx * coef[0]) / coef[1]
plt.plot(lx, ly, c='yellow')
plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'], marker = 'o', s=200, c='red')
plt.scatter(df_test_positive['Clump Thickness'],df_test_positive['Cell Size'], marker = 'x', s=150, c='black')
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
plt.show()

