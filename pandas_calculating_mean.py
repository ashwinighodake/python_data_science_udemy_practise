import numpy as np
import pandas as pd

df=pd.read_csv("/Users/ashwini/All_CSV_files/tips.csv")
print(df.head())
print(80*'*')
print(df['total_bill'].mean())
print(80*'*')

def yelp(price):
    if(price<10):
        return '$'
    elif price>=10 and price<30:
        return '$$'
    else:
        return '$$$'

df['yelp']=df['total_bill'].apply(yelp)
print(df['yelp'])
print(80*'*')


def Simple(num):
    return num*2

print(Simple(2))

df['total_bill'].apply(Simple)

#lambda num:num*2
print(80*'*')

print(df['total_bill'].apply(lambda num:num*2))


def quality(total_bill,tip):
    if(tip/total_bill>0.25):
        return "Generous"
    else:
        return "Others"
    
print(80*'*')

print(quality(16.99,1.01))
print(80*'*')

print(df[['total_bill','tip']].apply(lambda df:quality(df['total_bill'],df['tip']),axis=1))
print(80*'*')
df['Quality']=np.vectorize(quality)(df['total_bill'],df['tip'])
print(df['Quality'])