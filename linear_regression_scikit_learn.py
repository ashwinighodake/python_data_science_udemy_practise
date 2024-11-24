import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/Users/ashwini/All_CSV_files/Advertising.csv')
print(df.head())
df=df.drop('Unnamed: 0',axis=1)
print(80*'*')
print(df.head())

sns.pairplot(data=df)
#plt.show()
print(80*'*')

X=df.drop('Sales',axis=1)
print(X.head())
y=df['Sales']
print(80*'*')
print(y.head())

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
print(80*'*')
print('Length of dataframe:',len(df))
print('Length of X_train:',len(X_train))
print('Length of X_test:',len(X_test))
print('Length of y_train:',len(y_train))
print('Length of y_test:',len(y_test))
print(80*'*')

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)
print(model.predict(X_test))

