import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

theList =[1,2,3,4,5]
nb ,pb ,cb , tb ,nw ,pw ,cw =22, 1700, 200, 55, 0.1, 0.1, 0.5
nn ,basePrice ,imgPrice1 ,imgPrice2 ,priceOffset =23 ,91700 ,92600 ,92600 ,0
print(tb +(nb -nn) *nw +(pb -(imgPrice2-basePrice))/100 *pw +(cb -(imgPrice2-imgPrice1))/100 *cw +priceOffset)