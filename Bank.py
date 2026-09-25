import pandas as pd
import numpy as np

df = pd.read_excel('Banking_Dirty_Data_Analytics_Practice_10000.xlsx')

# Drop duplicates of all data
df = df.drop_duplicates()
# df.columns = df.columns.str.strip()

for col in df.select_dtypes(include=["object","str"]).columns:
    df[col] = df[col].str.strip()

# all string columne to remove extra columne
text_cols = df.select_dtypes(include=["object","str"]).columns
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
df["Account_Balance"] = df["Account_Balance"].fillna(0)

#Transaction Date
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format='mixed',dayfirst = False, errors='coerce')
df["Transaction_Date"] = df["Transaction_Date"].fillna(df["Transaction_Date"].mode()[0])

#Transaction Type 
df["Transaction_Type"] = df["Transaction_Type"].replace({"Withdrawl" : "Withdrawal", "Paymnt":"Payment"})

#Transaction Amount
df['Transaction_Amount'] = df['Transaction_Amount'].abs()
df['Transaction_Amount']=df["Transaction_Amount"].round()
#fill median value
median_Value = df["Transaction_Amount"].median()
df["Transaction_Amount"] = df["Transaction_Amount"].fillna(median_Value)

# Channel 
df["Channel"] = df["Channel"].replace({"Upi" : "UPI", "Atm" : "ATM", "Mobilebanking" : "Net Banking", "Internet Banking" : "Net Banking", "Mobile App" : "Net Banking"  })

#Transaction_Status
df["Transaction_Status"] = df["Transaction_Status"].replace({"Faild" : "Failed"})

df["Transaction_Status"] = df["Transaction_Status"].fillna("Success")

#KYC status 
df["KYC_Status"] = df["KYC_Status"].replace({"Pendng" : "Pending"})
df["KYC_Status"] = df["KYC_Status"].fillna("Verified")

# Phone number
df.loc[df["Phone"].str.len() != 10, "Phone"] = np.nan
df["Phone"] = df["Phone"].fillna("Unknown")

#Email
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Email valid pattern
df.loc[~df["Email"].str.match(pattern, na=False),"Email"] = np.nan
df["Email"] = df["Email"].fillna("UnknoWn")

#Barnch code
Branch_pattern = r'^\d+$'
df.loc[~df["Branch_Code"].astype(str).str.upper().str.match(Branch_pattern, na=False),"Branch_Code"] = np.nan
df["Branch_Code"] = df["Branch_Code"].fillna("Unkonwn")

#IFSC code
IFSC_pattern = r'^[A-Z]{4}0[A-Z0-9]{6}$'
df.loc[~df["Branch_Code"].astype(str).str.upper().str.match(IFSC_pattern, na=False),"IFSC_Code"] = np.nan
df["IFSC_Code"] = df["IFSC_Code"].fillna("Unknown")

df.to_excel("Baking_Clean_Data.xlsx", index=False)
