# A Dataframe is a table of columns & rows in a pandas thet we can easily restructure & filter. - A group of pandas series object that share same index.
import numpy as np
import pandas as pd

#df=pd.DataFrame(data,index,columns)

mydata = np.random.randint(0,101,(4,3))
myindex=['CA','NY','AZ','TX']
mycolumn=['Jan','Feb','Mar']

df=pd.DataFrame(mydata,myindex,mycolumn)
print(df)

df=pd.read_csv("/Users/ashwini/All_CSV_files/advertising .csv")
print("Information of csv file:",df.info())
print("First 5 rows in dataframe:",df.head())
print("Last 5 rows in dataframe:",df.tail())
print("all the description like count,mean,etc:",df.describe())
print("Column names of the dataframe:",df.columns)
print("Index of the dataframes:",df.index)
print("Description with transpose matrix:",df.describe().transpose())