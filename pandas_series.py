# Pandas is library for data analysis , It is extremly powerful table (Dataframe) system built off of numpy. 
# Series- series is data structure in pandas that holds an array of imformation along with a named index.
import numpy as np
import pandas as pd

myindex=['USA','Canada','Maxico']
mydata=[1776,1867,1821]
myseries=pd.Series(mydata,myindex)
print(myseries)

ages={'ABC':50,'XYZ':20,'WBC':10}
myseries=pd.Series(ages)
print(myseries)

q1={'Japan':80,'China':450,'India':200,'USA':250}
q2={'Brazil':100,'China':500,'India':210,'USA':200}

sale_q1=pd.Series(q1)
sale_q2=pd.Series(q2)

print(sale_q1)
print(sale_q2)

print(sale_q1+sale_q2)