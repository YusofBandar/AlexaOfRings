#ANN

#DATA PREPROCESSING
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
#import dataset
dataset = pd.read_csv("")
X = dataset.iloc[:].values
y = dataset.iloc[:].values

#encode data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

#split dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state = 0)

#Scale data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#BUILD ANN
import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

classifier.add(Dense(activation='relu', input_dim=, units=, kernal_initializer='uniform'))
classifier.add(Dense(activation='relu', units=, kernal_initializer='uniform'))
classifier.add(Dense(activation='softmax', units=5, kernal_initializer='uniform'))

classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
classifier.fit(X_train, y_train, batch_size=10, epochs=500)

#MAKE PREDICTIONS
