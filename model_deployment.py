import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error
import joblib

df=pd.read_csv('/Users/ashwini/All_CSV_files/Advertising.csv')
print(80*'*')
df=df.drop('Unnamed: 0',axis=1)
print(df.head())

X=df.drop('Sales',axis=1)
y=df['Sales']
print(X)
print(80*'*')
print(y)
print(80*'*')


#TRAIN         | VALIDATION          | HOLD OUT TEST
# 70%          |    15%              | 15%
# 1st split => 70/30
# 2nd spli => 50/50 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101)
X_validation,X_holdout_test,y_validation,y_holdout_test=train_test_split(X_test,y_test,test_size=0.5,random_state=101)
print('X_train value is:')
print(X_train)
print(len(X))
print(80*'*')
print(len(X_train))
print(80*'*')
print(len(X_test))
print(80*'*')
print(len(X_validation))
print(80*'*')
print(len(X_holdout_test))
print(80*'*')

# Model Training
model=RandomForestRegressor(n_estimators=30,random_state=101)
model.fit(X_train,y_train)
print(80*'*')
validation_prediction=model.predict(X_validation)


print(validation_prediction)

print(mean_absolute_error(y_validation,validation_prediction))
print(mean_squared_error(y_validation,validation_prediction)**0.5)


##Final performance metrics
holdout_predictions=model.predict(X_holdout_test)
print(mean_absolute_error(y_holdout_test,validation_prediction))
print(mean_squared_error(y_holdout_test,validation_prediction)**0.5)

final_model=RandomForestRegressor(n_estimators=30,random_state=101)
final_model.fit(X,y)
#final_model.predict([[230.1,37.8,69.2]])

joblib.dump(final_model,'final_model.pkl')

print(list(X.columns))
joblib.dump(list(X.columns),'col_names.pkl')

###Loading Model

new_columns=joblib.load('col_names.pkl')
print(new_columns)

loaded_model=joblib.load('final_model.pkl')

print(loaded_model.predict([[230.1,37.8,69.2]]))