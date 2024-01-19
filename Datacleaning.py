import pandas as pd

df = pd.read_excel(r'D:\1. APPS\Works\Playground\Python_learning\pandas\Projects_pandas\Data_Cleaning1\unorganized.xlsx')

df = df.drop_duplicates() 
df = df.drop(columns="Not_Useful_Column")

df["Last_Name"] = df["Last_Name"].str.strip("/._")
df["First_Name"] = df["First_Name"].str.rstrip(" ")
df["Phone_Number"] = df["Phone_Number"].str.replace('\D', '', regex=True) 

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:10])

df["Phone_Number"] = df["Phone_Number"].str.replace("nan--", "", regex=True)
df["Phone_Number"] = df["Phone_Number"].str.replace("--", "", regex=True)

df[["Street_Address", "State", "Zip_code"]] = df["Address"].str.split(',', expand=True)
df = df.drop(columns="Address")

df["Paying_Customer"] = df["Paying Customer"]
df["Paying_Customer"] = df["Paying_Customer"].str.replace("Yes", "Y",regex=True)
df["Paying_Customer"] = df["Paying_Customer"].str.replace("No", "N",regex=True)
df = df.drop(columns="Paying Customer")

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes", "Y",regex=True)
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No", "N",regex=True)
df["Do_Not_Contact"].fillna("", inplace=True)
df = df.replace("N/a", "")
df.fillna("", inplace=True)

for x in df.index:
    if df.loc[x,"Do_Not_Contact"] == "Y":
        df.drop(x, inplace=True)
        
for x in df.index:
    if df.loc[x,"Phone_Number"] == "":
        df.drop(x, inplace=True)

df = df.reset_index(drop=True)

print(df)

df.to_excel('Organized.xlsx')