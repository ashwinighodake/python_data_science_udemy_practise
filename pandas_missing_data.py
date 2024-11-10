import numpy as np
import pandas as pd

df=pd.read_csv("/Users/ashwini/All_CSV_files/movie_scores.csv")
print(df.head())
print(80*'*')

print(df.isnull())
print(80*'*')
print(df.notnull())
print(80*'*')
print(df[(df['pre_movie_score'].isnull()) & (df['first_name'].notnull())])
print(80*'*')
print(df.dropna())
print(80*'*')
print(df.dropna(thresh=1))
print(80*'*')
print(df.dropna(axis=1))
print(80*'*')
print(df.dropna(axis=0))
print(80*'*')
print(df.dropna(subset=['last_name']))
print(80*'*')

print("**********Filling the values**************")
print(df['pre_movie_score'].fillna(0))
print(80*'*')
df=df.fillna(df.mean)
print(df)


print("************Interpolation**********")

airline_fix={'first':100,'business':np.nan,'economy_plus':50,'economy':30}
ser=pd.Series(airline_fix)

print(ser.interpolate())