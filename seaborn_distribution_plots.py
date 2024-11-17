import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/Users/ashwini/All_CSV_files/dm_office_sales.csv')
print(df.head())

sns.rugplot(x='salary',data=df)
plt.show()

plt.figure(figsize=(5,8),dpi=200)
sns.rugplot(x='salary',data=df,height=0.5)
plt.show()

sns.displot(data=df,x='salary')
plt.show()

sns.displot(data=df,x='salary',bins=10)
plt.show()

sns.set(style='white')
sns.set(style='darkgrid')
sns.displot(data=df,x='salary',bins=20)
plt.show()

sns.set(style='whitegrid')
sns.displot(data=df,x='salary',bins=20)
plt.show()

sns.displot(data=df,x='salary',bins=20,color='red',edgecolor='blue',linewidth=4)
plt.show()

sns.histplot(data=df,x='salary')
plt.show()

sns.displot(data=df,x='salary',bins=20,kde=True)
plt.show()

sns.displot(data=df,x='salary',bins=20,kde=True,rug=True)
plt.show()

sns.kdeplot(data=df,x='salary')
plt.show()

print(np.random.seed(42))
sample_ages=np.random.randint(0,100,200)
print(sample_ages)

sample_ages=pd.DataFrame(data=sample_ages,columns=['age'])
print(sample_ages.head())

sns.rugplot(data=sample_ages,x='age')
plt.show()

sns.displot(data=sample_ages,x='age',rug=True,kde=True)
plt.show()

sns.kdeplot(data=sample_ages,x='age')
plt.show()

sns.kdeplot(data=sample_ages,x='age',clip=[0,100],bw_adjust=0.6,shade=True)
plt.show()