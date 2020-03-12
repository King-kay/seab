import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
from pandas import DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('gapminder-FiveYearData.csv')

df.describe()
df.head()
df.info()

df2 = df[['year', 'continent', 'lifeExp']]
print df2.shape
print (df2.head())
pd.pivot_table(df2, values='lifeExp', index=['year'], columns='continent')
print df2
sns.heatmap(df2, cmap='YlGnBu')
sns.heatmap(df2,annot=True, fmt='d').get_figure().savefig("gapmind.png")
