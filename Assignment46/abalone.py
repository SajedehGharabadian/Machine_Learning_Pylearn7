import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from numpy.linalg import inv
from perceptron import Perceptron


data = pd.read_csv('Dataset/abalone.data.csv')
data.columns = ['Sex','Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight','Rings']

X = data['Length'].values
Y = data['Diameter'].values

X = np.array(X)
X = X.reshape((X.shape[0],1))
Y = np.array(Y)
Y = Y.reshape((Y.shape[0],1))

print(X.shape)
print(Y.shape)

X_train,X_test,y_train,y_test = train_test_split(X,Y)

perceptron = Perceptron(epochs=50,learning_rate_w=0.001,learning_rate_b=0.01)
perceptron.fit(X_train,y_train)

