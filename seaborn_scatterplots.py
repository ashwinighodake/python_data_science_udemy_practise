import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('/Users/ashwini/All_CSV_files/dm_office_sales.csv')
print(df.head())

plt.figure(figsize=(12,4),dpi=150)
sns.scatterplot(x='salary',y='sales',data=df)
plt.show()


sns.scatterplot(x='salary',y='sales',data=df,hue='level of education')
plt.show()

sns.scatterplot(x='salary',y='sales',data=df,hue='salary')
plt.show()

sns.scatterplot(x='salary',y='sales',data=df,hue='level of education',palette='Dark2')
plt.show()

sns.scatterplot(x='salary',y='sales',data=df,hue='level of education',size='salary')
plt.show()

sns.scatterplot(x='salary',y='sales',data=df,s=200)
plt.show()

sns.scatterplot(x='salary',y='sales',data=df,s=200,alpha=0)
plt.show()

sns.scatterplot(x='salary',y='sales',data=df,s=200,alpha=0.5)
plt.show()

sns.scatterplot(x='salary',y='sales',data=df,s=200,alpha=1)
plt.show()

sns.scatterplot(x='salary',y='sales',data=df,s=200,style='level of education')
plt.show()

sns.scatterplot(x='salary',y='sales',data=df,style='level of education',hue='level of education')
plt.show()
#plt.savefig('my_scatterplot.jpg')