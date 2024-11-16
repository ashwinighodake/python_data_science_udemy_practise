import numpy as np
import pandas as pd

df=pd.read_csv('/Users/ashwini/Downloads/Sales_Funnel_CRM.csv')
licenses=df[['Company','Product','Licenses']]
print(pd.pivot(data=licenses,index='Company',columns='Product',values='Licenses'))