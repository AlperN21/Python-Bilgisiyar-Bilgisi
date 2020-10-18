#Buradaki bazı kısımlar açık kaynak kodlardır.

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from xgboost import XGBClassifier
import xgboost as xgb
from sklearn.metrics import accuracy_score

dataset_len = 40000000 #veri listemizi ayarlıyoruz.
dlen = int(dataset_len/2)
X_11 = pd.Series(np.random.normal(2,2,dlen))
X_12 = pd.Series(np.random.normal(9,2,dlen))
X_1 = pd.concat([X_11, X_12]).reset_index(drop=True)
X_21 = pd.Series(np.random.normal(1,3,dlen))
X_22 = pd.Series(np.random.normal(7,3,dlen))
X_2 = pd.concat([X_21, X_22]).reset_index(drop=True)
X_31 = pd.Series(np.random.normal(3,1,dlen))
X_32 = pd.Series(np.random.normal(3,4,dlen))
X_3 = pd.concat([X_31, X_32]).reset_index(drop=True)
X_41 = pd.Series(np.random.normal(1,1,dlen))
X_42 = pd.Series(np.random.normal(5,2,dlen))
X_4 = pd.concat([X_41, X_42]).reset_index(drop=True)
Y = pd.Series(np.repeat([0,1],dlen))
df = pd.concat([X_1, X_2, X_3, X_4, Y], axis=1)
df.columns = ['X1', 'X2', 'X3', 'X_4', 'Y']
df.head()

train_size = 0.80
X = df.drop(['Y'], axis = 1).values
y = df['Y']

#Labelencoder nesnesi kelime etiketlerinin nasıl anlaşılacağını bilir.
label_encoder = preprocessing.LabelEncoder()

y = label_encoder.fit_transform(y)

num_rows, num_columns = df.shape
delim_index = int(num_rows * train_size)

X_train, y_train = X[:delim_index, :], y[:delim_index]
X_test, y_test = X[delim_index:, :], y[delim_index:]


print('X_train dimensions: ', X_train.shape, 'y_train: ', y_train.shape)
print('X_test dimensions:', X_test.shape, 'y_validation: ', y_test.shape)

# Checking dimensions in percentages parametreleri çekiyoruz
total = X_train.shape[0] + X_test.shape[0]
print('X_train Percentage:', (X_train.shape[0]/total)*100, '%')
print('X_test Percentage:', (X_test.shape[0]/total)*100, '%')

#%%time

model = XGBClassifier(tree_method='hist')
model.fit(X_train, y_train)

sk_pred = model.predict(X_test)
sk_pred = np.round(sk_pred)
sk_acc = round(accuracy_score(y_test, sk_pred), 2)
print("XGB accuracy using Sklearn:", sk_acc*100, '%')
