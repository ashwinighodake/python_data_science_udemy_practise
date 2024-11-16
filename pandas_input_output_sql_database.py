import numpy as np
import pandas as pd
from sqlalchemy import create_engine
temp_db=create_engine('sqlite:///memory:')
df=pd.DataFrame(data=np.random.randint(low=0,high=100,size=(4,4)),columns=['a','b','c','d'])
print(df)
#df.to_sql(name='new_table',con=temp_db)
print(pd.read_sql(sql='new_table',con=temp_db))
print(pd.read_sql_query(sql='select a,c from new_table',con=temp_db))