# -*- coding: utf-8 -*-
"""SONAR Rock vs Mine Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-63y9kZ1t8CBsufGK2fpjD7lEWyywViM

Importing the dependencier
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Data Processing"""

#Loading the dataset to a pandas Dataframe
sonar_data=pd.read_csv('/content/sonar data.csv',header=None)

sonar_data.head()

#number of row and columns
sonar_data.shape

sonar_data.describe()

sonar_data[60].value_counts()

"""M--> Mine
R-->Rock
"""

sonar_data.groupby(60).mean()

# seperating data and Lables
X= sonar_data.drop(columns=60,axis=1)
Y=sonar_data[60]

print(X)
print(Y)

"""TRAINING AND TEST DATA"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

print(X_train)
print(Y_train)

"""Model Training (LOGISTIC REGRESSION)"""

model=LogisticRegression()

#training the Logistic Regression with training data
model.fit(X_train,Y_train)

model.fit(X_train,Y_train)

"""Model Evaluation"""

#accuracy on training data
X_train_prediction=model.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

#accurac on training data
X_train_prediction=model.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

print('Accuracy on training data : ',training_data_accuracy)

#accurac on test data
X_test_prediction=model.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)

print('Accuracy on test data : ',test_data_accuracy)

"""Making a Predictive System"""

input_data = (0.0352,0.0116,0.0191,0.0469,0.0737,0.1185,0.1683,0.1541,0.1466,0.2912,0.2328,0.2237,0.2470,0.1560,0.3491,0.3308,0.2299,0.2203,0.2493,0.4128,0.3158,0.6191,0.5854,0.3395,0.2561,0.5599,0.8145,0.6941,0.6985,0.8660,0.5930,0.3664,0.6750,0.8697,0.7837,0.7552,0.5789,0.4713,0.1252,0.6087,0.7322,0.5977,0.3431,0.1803,0.2378,0.3424,0.2303,0.0689,0.0216,0.0469,0.0426,0.0346,0.0158,0.0154,0.0109,0.0048,0.0095,0.0015,0.0073,0.0067)
# changing the input_data to a numpy arrray
input_data_as_numpy_array = np.asarray(input_data)

# reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction=model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]=='R'):
  print('The object is a Rock')
else:
  print('The object is a mine')

