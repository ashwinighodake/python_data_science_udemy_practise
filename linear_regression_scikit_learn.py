import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/Users/ashwini/All_CSV_files/Advertising.csv')
print(df.head())
df=df.drop('Unnamed: 0',axis=1)
print(80*'*')
print(df.head())

#sns.pairplot(data=df)
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
test_predictions=model.predict(X_test)

from sklearn.metrics import mean_absolute_error,mean_squared_error
print(df['Sales'].mean())
mean_abs_error=mean_absolute_error(y_test,test_predictions)  #10% error
print(mean_abs_error)
mean_sq_error=mean_squared_error(y_test,test_predictions)
print(mean_sq_error)

mean_rmsq_error=np.sqrt(mean_squared_error(y_test,test_predictions))
print(mean_rmsq_error)

test_residuals=y_test-test_predictions
#print(test_residuals)
sns.scatterplot(x=y_test,y=test_residuals)
plt.axhline(y=0,color='r',ls='--')
plt.show()

sns.displot(test_residuals,bins=25,kde=True)
plt.show()

import scipy as sp
fig,ax=plt.subplots(figsize=(6,8),dpi=100)
_=sp.stats.probplot(test_residuals,plot=ax)
plt.show()