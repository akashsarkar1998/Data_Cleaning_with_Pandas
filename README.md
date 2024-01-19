# Pandas Data Cleaning Project 
## Overview

This small data cleaning project involves processing an Excel file based on specific client requirements. The goal is to filter and display only those rows containing valid phone numbers. The project utilizes the powerful Pandas library in Python to achieve efficient data manipulation and cleaning.

---
### Project Structure:
- **Datacleaning.py :** Python script containing the data cleaning logic.
- **unorganized.xlsx :**  Input Excel file provided by the client.
- **Organized.xlsx :** Output Excel file containing cleaned data with only valid phone numbers.

### `Project code:`
Here I am providing my codes as well! feel free to check.
```python
import pandas as pd

# Step 1: Read the Excel file into a Pandas DataFrame
df = pd.read_excel(r'D:\1. APPS\Works\Playground\Python_learning\pandas\Projects_pandas\Data_Cleaning1\unorganized.xlsx')

# Step 2: Remove duplicate rows
df = df.drop_duplicates()

# Step 3: Drop a column that is not useful
df = df.drop(columns="Not_Useful_Column")

# Step 4: Strip leading and trailing characters in the 'Last_Name' column
df["Last_Name"] = df["Last_Name"].str.strip("/._")

# Step 5: Remove trailing whitespaces in the 'First_Name' column
df["First_Name"] = df["First_Name"].str.rstrip(" ")

# Step 6: Remove non-digit characters from the 'Phone_Number' column
df["Phone_Number"] = df["Phone_Number"].str.replace('\D', '', regex=True)

# Step 7: Format the 'Phone_Number' column as XXX-XXX-XXXX
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:10])

# Step 8: Remove specific patterns from the 'Phone_Number' column
df["Phone_Number"] = df["Phone_Number"].str.replace("nan--", "", regex=True)
df["Phone_Number"] = df["Phone_Number"].str.replace("--", "", regex=True)

# Step 9: Split the 'Address' column into 'Street_Address', 'State', and 'Zip_code' columns
df[["Street_Address", "State", "Zip_code"]] = df["Address"].str.split(',', expand=True)
df = df.drop(columns="Address")

# Step 10: Clean and format the 'Paying_Customer' column
df["Paying_Customer"] = df["Paying Customer"]
df["Paying_Customer"] = df["Paying_Customer"].str.replace("Yes", "Y", regex=True)
df["Paying_Customer"] = df["Paying_Customer"].str.replace("No", "N", regex=True)
df = df.drop(columns="Paying Customer")

# Step 11: Clean and format the 'Do_Not_Contact' column
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes", "Y", regex=True)
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No", "N", regex=True)
df["Do_Not_Contact"].fillna("", inplace=True)
df = df.replace("N/a", "")
df.fillna("", inplace=True)

# Step 12: Remove rows where 'Do_Not_Contact' is 'Y'
for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == "Y":
        df.drop(x, inplace=True)

# Step 13: Remove rows where 'Phone_Number' is empty
for x in df.index:
    if df.loc[x, "Phone_Number"] == "":
        df.drop(x, inplace=True)

# Step 14: Reset the DataFrame index
df = df.reset_index(drop=True)

# Step 15: Display the organized DataFrame
print(df)

# Step 16: Save the organized DataFrame to a new Excel file
df.to_excel('Organized.xlsx')

``` 



### Requirements:
1. `Python 3.11.5`
2. `Pandas Library`

### Contributor:
Akash Sarkar akashsarkarcob98@gmail.com  
##### My Linkedin profile: &nbsp; [Akash's-Linkedin-Account][Linkedin_Account]

Feel free to contribute or provide feedback!


<!--Linkedin profile link here:-->
[Linkedin_Account]: https://www.linkedin.com/in/akash-sarkar59/