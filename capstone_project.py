import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fandango=pd.read_csv('/Users/ashwini/All_CSV_files/fandango_scrape.csv')
print(fandango.head())
print(fandango.info())
print(fandango.describe())

sns.scatterplot(data=fandango,y='VOTES',x='RATING')
plt.show()

print('Correlation between columns:')
print(fandango.corr(numeric_only=True))

fandango['Year']=fandango['FILM'].apply(lambda title:title.split('(')[-1].replace(')',''))
print(fandango.head())

print(fandango['Year'].value_counts())

sns.countplot(data=fandango,x='Year')
plt.show()

print(fandango.nlargest(10,'VOTES'))
print(80*'*')
print("How many movies having zero votes:")
no_votes=fandango['VOTES']==0
print(no_votes.sum())

print(80*'*')
print("Create dataframe only reviewed films by removing any films that have zero votes")
reviewed_films=fandango[fandango['VOTES']>0]
print(reviewed_films.head())

print(80*'*')
print("Create a kde plot that displays , the true user rating may be slightly different than the rating shown to user. Let's visualize this difference in distribution")

plt.figure(figsize=(10,6),dpi=150)
sns.kdeplot(data=reviewed_films,x='RATING',clip=[0,5],label='True Rating',fill=True)
sns.kdeplot(data=reviewed_films,x='STARS',clip=[0,5],label='Stars Displayed',fill=True)
plt.legend(loc=(0.8,1.05))
plt.show()

print(80*'*')
print("Create new column of the difference between STARS displayed versus true rating. Calculate the difference with stars-rating and round this differences to the nearest decimal point")
reviewed_films['Difference']=reviewed_films['STARS']-reviewed_films['RATING']
reviewed_films['Difference']=reviewed_films['Difference'].round(2)
print(reviewed_films)

print(80*'*')
print("Create countplot to display the number of times a certain differences occurs:")
sns.countplot(data=reviewed_films,x='Difference',palette='magma')
plt.show()

print(80*'*')
print("What movie had this close to 1 star differencial:")
print(reviewed_films[reviewed_films['Difference']==1])
