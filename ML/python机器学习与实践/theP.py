import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

bn ,blc ,btc ,wn ,wc =24, 8, 8, 0.3, 0.25
print(btc +(23 -bn) *wn +(blc -10) *wc)