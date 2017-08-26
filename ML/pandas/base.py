import numpy as np
import pandas as pd

dropList =[1,2,5]

data = pd.read_csv('1.csv')
print(data.drop(dropList))
print('-------')

dropList =['ll45p' ,'lln' ,'llw' ,'llp']
print(data.drop(dropList ,axis =1))
print('-------')

