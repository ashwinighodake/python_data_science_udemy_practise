import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/Users/ashwini/All_CSV_files/StudentsPerformance.csv')
print(df.head())

sns.jointplot(data=df,x='math score',y='reading score')
plt.show()

sns.jointplot(data=df,x='math score',y='reading score',kind='hex')
plt.show()

sns.jointplot(data=df,x='math score',y='reading score',kind='kde',shade=True)
plt.show()

sns.jointplot(data=df,x='math score',y='reading score',hue='gender')
plt.show()

sns.pairplot(data=df)
plt.show()

sns.pairplot(data=df,hue='gender')
plt.show()

sns.pairplot(data=df,hue='gender',diag_kind='hist')
plt.show()

sns.pairplot(data=df,hue='gender',corner=True)
plt.show()