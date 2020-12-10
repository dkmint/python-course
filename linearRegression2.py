import pandas as pd
import numpy as np
import seaborn as sns
import sklearn.datasets as data
from sklearn.linear_model import LinearRegression

wine = data.load_wine()
type(wine)
wine.keys()
print(wine.DESCR)
wine.data
wine.feature_names
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['wine_type'] = wine.target
wine.target
df.info()
df.head()
sns.pairplot(df)
# plt.show()
reg = LinearRegression()
reg
X = df['proline']
y = df['alcohol']
X # here X is Pandas's series; so it's like 1D; it's wrong, we need to convert data frame.
reg.fit(X,y)
# Cause of error: sklearn requirements is X should be a 2D array, or Pandas DataFrame, or a Matrix; 
#it should be 2D tabel of data

#y can be 1D array or 1D DataFrame
X = df[['proline']]
y = df['alcohol']
X # here X is Pandas's series; so it's like 1D; it's wrong, we need to convert data frame.
reg.fit(X, y)
pred = reg.predict(X) # save this into pred variable
