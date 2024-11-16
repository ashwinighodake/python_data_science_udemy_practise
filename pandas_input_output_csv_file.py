import pandas as pd

df=pd.read_csv('/Users/ashwini/All_CSV_files/tips.csv')
print(df)

df.to_csv('/Users/ashwini/python_data_science_udemy_practise/python_data_science_udemy_practise/tips_practice.csv')
