import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/Users/ashwini/All_CSV_files/dm_office_sales.csv')
print(df.head())

sns.scatterplot(x='salary',y='sales',data=df)
plt.show()