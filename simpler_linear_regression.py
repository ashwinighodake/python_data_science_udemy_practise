import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/Users/ashwini/All_CSV_files/Advertising.csv')
print(df.head())
print(80*'*')

df['total_spend']=df['TV']+df['Radio']+df['Newspaper']
print(df.head())

sns.scatterplot(data=df,x='total_spend',y='Sales')
plt.show()

sns.regplot(data=df,x='total_spend',y='Sales')
plt.show()
print(80*'*')

X=df['total_spend']
y=df['Sales']

print(np.polyfit(X,y,deg=1)) #y=B1x+B0

potential_spend=np.linspace(0,500,100)
predicted_sales=0.04868788*potential_spend+4.24302822
print(predicted_sales)
sns.scatterplot(x='total_spend',y='Sales',data=df)
plt.plot(potential_spend,predicted_sales,color='red')
plt.show()

print(80*'*')
spend=200
predicted_sales=0.04868788*spend+4.24302822
print(predicted_sales)

print(80*'*')
print(np.polyfit(X,y,3)) #y=B3**3+B2**2+B1x+B0
print(80*'*')
pot_spend=np.linspace(0,500,100)
print(pot_spend)
pred_sales=3.07615033e-07*pot_spend**3-1.89392449e-04*pot_spend**2+8.20886302e-02*pot_spend+2.70495053e+00
print(pred_sales)
sns.scatterplot(x='total_spend',y='Sales',data=df)
plt.plot(pot_spend,pred_sales,color='red')
print(plt.show())