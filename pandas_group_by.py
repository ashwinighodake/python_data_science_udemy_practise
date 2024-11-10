import numpy as np
import pandas as pd

df=pd.read_csv("/Users/ashwini/All_CSV_files/mpg.csv")
print(df.head())
print(80*'*')
print(df['model_year'].value_counts())
print(80*'*')
print(df['model_year'].unique())
print(df.groupby('model_year').mean)
print(df.groupby('model_year').describe())