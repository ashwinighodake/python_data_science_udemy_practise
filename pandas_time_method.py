import numpy as np
import pandas as pd
from datetime import datetime

myyear=2015
mymonth=1
myday=1
myhour=2
mymin=30
mysec=15
mydate=datetime(myyear,mymonth,myday)
print(mydate)

mydate=datetime(myyear,mymonth,myday,myhour,mymin,mysec)
print(mydate)
print(mydate.year)

myser=pd.Series(['Nov 3,1990','2000-01-01',None])
print(myser)
print(pd.to_datetime(myser))
print(80*'*')
timeser=pd.to_datetime(myser)
obvio_euro_date='31-12-2000'
print(80*'*')
print(pd.to_datetime(obvio_euro_date))
print(80*'*')

euro_date='10-12-2000'
print(pd.to_datetime(euro_date,dayfirst=True))
print(80*'*')

style_date='12--Dec--2000'
print(pd.to_datetime(style_date,format='%d--%b--%Y'))
print(80*'*')

custom_date='12th of Dec 2000'
print(pd.to_datetime(custom_date))
print(80*'*')
