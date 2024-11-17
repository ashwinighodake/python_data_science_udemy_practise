import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/Users/ashwini/All_CSV_files/StudentsPerformance.csv')
print(df.head())

sns.catplot(data=df,x='gender',y='math score',kind='box')
plt.show()

sns.catplot(data=df,x='gender',y='math score',kind='box',hue='lunch')
plt.show()

sns.catplot(data=df,x='gender',y='math score',kind='box',row='test preparation course',col='lunch')
plt.show()

sns.catplot(data=df,x='gender',y='math score',kind='box',row='race/ethnicity',col='lunch')
plt.show()

sns.catplot(data=df,x='gender',y='math score',kind='violin',row='race/ethnicity',col='lunch')
plt.show()

g=sns.PairGrid(df,hue='gender')
g=g.map_upper(sns.scatterplot)
g=g.map_diag(sns.histplot)
g=g.map_lower(sns.kdeplot)
plt.show()