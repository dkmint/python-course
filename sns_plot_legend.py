import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
%matplotlib inline

sns.lmplot('weight', 'mpg', data=df, fit_reg=False, aspect=2, size=4, hue='cylinders')
plt.show()
