import pandas as pd

df = pd.read_excel('Banking_Dirty_Data_Analytics_Practice_10000.xlsx')

print(df.info())

import os
print(os.getcwd())
print(os.listdir())