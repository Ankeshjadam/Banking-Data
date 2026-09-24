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
mean_Income =  round(df.loc[df["Annual_Income"] > 0,"Annual_Income"].mean(),2)
df["Annual_Income"] = df["Annual_Income"].mask(df["Annual_Income"]<= 0, mean_Income)
df["Annual_Income"] = df["Annual_Income"].fillna(mean_Income)
df["Annual_Income"] = df["Annual_Income"].round(2)

#Account balence
df["Account_Balance"] = df["Account_Balance"].round(2)
print(df["Account_Balance"].head(10))






print(df.info())