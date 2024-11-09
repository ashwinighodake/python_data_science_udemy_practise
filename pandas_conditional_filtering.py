import numpy as np
import pandas as pd

df=pd.read_csv("/Users/ashwini/All_CSV_files/tips.csv")
print(df.head())
print(80*'*')
print(df[(df['total_bill']>30)&(df['sex']=='Male')])
options=['Sat','Sun']
print(80*'*')
print(df['day'].isin(options))
print(80*'*')
print("last 4 digits getting from the strring")
print(80*'*')
print(str(1234567890)[0])
print(str(1234567890)[-4:])

print(80*'*')

def last_four(num):
    return str(num)[-4:0]
print(80*'*')

print(df['CC Number'].apply(last_four))
print(80*'*')
