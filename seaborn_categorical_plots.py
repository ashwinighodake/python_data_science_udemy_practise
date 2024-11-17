import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/Users/ashwini/All_CSV_files/dm_office_sales.csv')
print(df.head())

plt.figure(figsize=(10,5))
sns.countplot(data=df,x='division')
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(data=df,x='level of education',hue='division')
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(data=df,x='level of education',y='salary',estimator=np.mean,ci='sd')
plt.show()

sns.barplot(data=df,x='level of education',y='salary',estimator=np.mean,errorbar='sd',hue='division')
plt.legend(bbox_to_anchor=(1.05,1))
plt.show()