import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/Users/ashwini/All_CSV_files/StudentsPerformance.csv')
print(df.head())

sns.boxplot(data=df,y='math score',)
plt.show()

plt.figure(figsize=(10,4),dpi=150)
sns.boxplot(data=df,y='math score',x='test preparation course')
plt.show()

plt.figure(figsize=(10,6),dpi=150)
sns.boxplot(data=df,y='reading score',x='parental level of education',hue='test preparation course')
plt.legend(bbox_to_anchor=(0.8,1))
plt.show()

plt.figure(figsize=(10,8),dpi=150)
sns.boxplot(data=df,y='reading score',x='parental level of education',hue='test preparation course',palette='Set2')
plt.legend(bbox_to_anchor=(0.8,1))
plt.show()

plt.figure(figsize=(10,8),dpi=150)
sns.violinplot(data=df,y='reading score',x='parental level of education',hue='test preparation course',palette='Set2')
plt.legend(bbox_to_anchor=(1,1.5))
plt.show()

plt.figure(figsize=(10,8),dpi=150)
sns.violinplot(data=df,x='reading score',y='parental level of education',hue='test preparation course',palette='Set2')
plt.legend(bbox_to_anchor=(0.8,1))
plt.show()

plt.figure(figsize=(10,8),dpi=150)
sns.violinplot(data=df,x='reading score',y='parental level of education',hue='test preparation course',palette='Set2',split=True,inner=None)
plt.show()

sns.swarmplot(data=df,x='math score',size=2)
plt.show()

plt.figure(figsize=(8,4),dpi=150)
sns.swarmplot(data=df,x='math score',y='gender',size=2,hue='test preparation course')
plt.legend(bbox_to_anchor=(1.35,0.5))
plt.show()

sns.boxenplot(x='math score',y='test preparation course',data=df)
plt.show()

sns.boxenplot(x='math score',y='test preparation course',data=df,hue='gender')
plt.show()