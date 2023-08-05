import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_boston
from sklearn import datasets
from Bosto_house_Price.Percpeptron import Perceptron
from sklearn.model_selection import train_test_split

data_houses = load_boston()
data = pd.DataFrame(data_houses.data, columns=data_houses.feature_names)
data['MEDV'] = data_houses.target

X = np.array(data[['RM', 'AGE']])
Y = np.array(data[['MEDV']])
Y = Y.reshape(-1,1)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y)


perceptron = Perceptron(learning_rate_w=0.000001,learning_rate_b=0.001,epochs=10)
perceptron.fit(X_train, Y_train)