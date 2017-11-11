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


#BUILD ANN
import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

classifier.add(Dense(activation='relu', input_dim=, units=, kernal_initializer='uniform'))
classifier.add(Dense(activation='relu', units=, kernal_initializer='uniform'))
classifier.add(Dense(activation='softmax', units=5, kernal_initializer='uniform'))


#MAKE PREDICTIONS
