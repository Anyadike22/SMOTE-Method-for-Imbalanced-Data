!pip install imblearn
     

import pandas as pd
import seaborn as sns 
from matplotlib import pyplot as plt
import numpy as np
%matplotlib inline
     

df = pd.read_csv('spaceship_imbalanced.csv')
     

df.head()
     

sns.countplot(x='Transported', data=df)
plt.show()
     

from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler
     

X = df.drop('Transported', axis=1)
y = df['Transported']
     

resamp = RandomUnderSampler()
balX, baly = resamp.fit_resample(X,y)
     

sns.countplot(x=baly)
plt.show()
