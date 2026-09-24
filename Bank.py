import pandas as pd
import numpy as np

df = pd.read_excel('Banking_Dirty_Data_Analytics_Practice_10000.xlsx')

# Drop duplicates of all data
df = df.drop_duplicates()

text_cols = df.select_dtypes(include="object").columns
df[text_cols] = df[text_cols].apply(lambda col : col.str.strip().str.title() )

## age columne 
df["Age"] = df["Age"].fillna(0)
df["Age"] = df["Age"].astype(int).fillna(df["Age"].mean())

# Gender fill enpty to unkown
df["Gender"] = df["Gender"].replace({"F":"Female","M":"Male"})
df["Gender"] = df["Gender"].fillna("Uknown")

#State 
df["State"] = df["State"].replace({"Madhya Pradseh":"Madhya Pradesh", "Tamil Nadu" : "Tamilnadu"})

#Account Type columne
df["Account_Type"] = df["Account_Type"].replace({"Curent" : "Current", "Saving" : "Savings", "Savigs" : "Savings"})

#Employment Type
df["Employment_Type"] = df["Employment_Type"].replace({"Self-Employed" : "Self Employed"})

# #Annual income
# df["Annual_Income"] = (df["Annual_Income"] <= 0).fillna(df["Annual_Income"].mean())
# df["Annual_Income"] = df["Annual_Income"].fillna(df["Annual_Income"].mean())

# print(df["Annual_Income"].head())






print(df.info())





