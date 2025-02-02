import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(80*'*')
df=pd.read_csv('/Users/ashwini/All_CSV_files/Advertising.csv')
df=df.drop('Unnamed: 0',axis=1)
print(df.head())
print(80*'*')

X=df.drop('Sales',axis=1)
y=df['Sales']
print(X.head())
print(y.head())
print(80*'*')

from sklearn.preprocessing import PolynomialFeatures
polynomial_converter=PolynomialFeatures(degree=2,include_bias=False)  
polynomial_converter.fit(X)
poly_features=polynomial_converter.transform(X)
print(X.shape)
print(X.iloc[0])
print(poly_features[0])
print(polynomial_converter.fit_transform(X))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(poly_features,y,test_size=0.33,random_state=101)

from sklearn.linear_model import LinearRegression
model=LinearRegression()

model.fit(X_train,y_train)
test_predictions=model.predict(X_test)
print(80*'*')
print(test_predictions)

#model.coef_

from sklearn.metrics import mean_absolute_error,mean_squared_error

MAE=mean_absolute_error(y_test,test_predictions)
MSE=mean_squared_error(y_test,test_predictions)
RMSE=np.sqrt(MSE)

print(80*'*')
print("Mean Absolute error:",MAE)
print("Mean Squared error:",MSE)
print("Root Mean squared error:",RMSE)

#Create the different order poly
# split poly feat train / test
# fit on train
# store /save the RMSE for bothhe train and test
# Plot the results(error vs Ploy order)
train_rmse_errors=[]
test_rmse_errors=[]

for d in range(1,10):
    poly_converter=PolynomialFeatures(degree=d,include_bias=False)
    poly_features=poly_converter.fit_transform(X)
    X_train,X_test,y_train,y_test=train_test_split(poly_features,y,test_size=0.3,random_state=101)

    model=LinearRegression()
    model.fit(X_train,y_train)
    train_pred=model.predict(X_train)
    test_pred=model.predict(X_test)

    train_rmse=np.sqrt(mean_absolute_error(y_train,train_pred))
    test_rmse=np.sqrt(mean_absolute_error(y_test,test_pred))

    train_rmse_errors.append(train_rmse)
    test_rmse_errors.append(test_rmse)

print(train_rmse_errors)
print(test_rmse_errors)

plt.plot(range(1,6),train_rmse_errors[:5],label='TRAIN RMSE')
plt.plot(range(1,6),test_rmse_errors[:5],label='TEST RMSE')
plt.xlabel('Degree of Poly')
plt.ylabel('RMSE')
plt.legend()
plt.show()

final_poly_converter=PolynomialFeatures(degree=3,include_bias=False)
final_model=LinearRegression()

full_converted_X=final_poly_converter.fit_transform(X)
final_model.fit(full_converted_X,y)

from joblib import dump,load
dump(final_model,'final_poly_model.joblib')

dump(final_poly_converter,'final_converter.joblib')
load_converter=load('final_converter.joblib')
load_model=load('final_poly_model.joblib')

campaign=[[149,22,12]]
transform_data=load_converter.fit_transform(campaign)
print(80*'*')
print(transform_data)
print(80*'*')

print(load_model.predict(transform_data))


