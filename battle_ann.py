#PART 1 - DATA PREPROCESSING

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('BattleData.csv')
X = dataset.iloc[:, :5].values
y = dataset.iloc[:, 5].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)

"""Feature Scaling - minimises risk of 1 independent variable dominating in the ANN 
and ease heavy computations on your machine"""
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#PART 2 - MAKING THE ARTIFICIAL NEURAL NETWORK

#Importing the Keras library and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

#Initialising the ANN
classifier = Sequential()

#Adding the input layer and the first hidden layer
classifier.add(Dense(activation = 'relu', input_dim = 5, units = 3, kernel_initializer = 'uniform'))

#Adding a second hidden layer
classifier.add(Dense(activation = 'relu', units = 3, kernel_initializer = 'uniform'))

#Adding the output layer
"""Use softmax activation function for output layer if more than 1 category - otherwise sigmoid"""
classifier.add(Dense(activation = 'sigmoid', units = 1, kernel_initializer = 'uniform'))

#Compiling the ANN
"""Loss function if more than 1 output node is called 'categorical_crossentropy'
otherwise if binary(either 1 or 0) use 'binary_crossentropy'"""
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#Fitting the ANN to training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)

#PART 3 - MAKING THE PREDICTIONS AND EVALUATING THE MODEL

# Predicting the Test set results
y_pred = classifier.predict(X_test)
#Categorise y_pred as being True or False (i.e. 1 or 0) for the confusion matrix
y_pred = (y_pred > 0.5)


new_prediction = classifier.predict(sc.transform(np.array([[0,1,1,0,0]])))
new_prediction = (new_prediction > 0.5)


