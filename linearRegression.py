import pandas as pd
import numpy as np
import seaborn as sns
import sklearn.datasets as data

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
