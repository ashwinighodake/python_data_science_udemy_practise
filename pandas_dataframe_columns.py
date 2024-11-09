import numpy as np
import pandas as pd

df=pd.read_csv("/Users/ashwini/All_CSV_files/tips.csv")
print(df.head())
print(df['total_bill'])
print("Two columns in the csv file:",df[['total_bill','tip']])
print("Addition of two columns in csv:",df['total_bill']+df['tip'])

df['tip_percentage']=100*df['tip']/df['total_bill']
print("In dataframe percentage column gets added:",df.head())

print(df.drop('tip_percentage',axis=1))
print(df.head())

df=df.drop('tip_percentage',axis=1)
print(df.head())

print(df.shape)  # It will show number of column & rows.

df.set_index('price_per_person',inplace=True)
print(df.head())

df=df.reset_index()
print(df)

print(df.iloc[0])
df=df.set_index('Payment ID')
print(df.loc['Sun2959'])

print(df.iloc[0:4])
#one_row=df.iloc[0]