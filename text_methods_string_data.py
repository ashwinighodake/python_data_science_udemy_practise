import numpy as np
import pandas as pd

email='joseph@email.com'
print(email.split('@'))

names=pd.Series(['andrew','bobo','claire','david','5'])
print(names.str.upper())

print(email.isdigit())
print(names.str.isdigit())
tech_finance=['GOOG,APPL,AMZN','JPM,BAC,GS']

print(len(tech_finance))
tickers=pd.Series(tech_finance)
print(tickers)

print(tickers.str.split(','))

print(tickers.str.split(',',expand=True))

messy_names=pd.Series(['andrew',"bo;bo","claire   "])
print(messy_names)
print(messy_names.str.replace(';',''))

print(messy_names.str.replace(';','').str.strip())