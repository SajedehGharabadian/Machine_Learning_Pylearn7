import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from perceptron import Perceptron
from sklearn.model_selection import train_test_split


X, Y, coef = datasets.make_regression(n_samples=500,#number of samples
                                      n_features=1,#number of features
                                      n_informative=1,#number of useful features 
                                      noise=10,#bias and standard deviation of the guassian noise
                                      coef=True,#true coefficient used to generated the data
                                      random_state=0) #set for same data points for each run

# Scale feature x (years of experience) to range 0..20
X = np.interp(X, (X.min(), X.max()), (0, 20))

# Scale target y (salary) to range 20000..150000 
Y = np.interp(Y, (Y.min(), Y.max()), (20000, 150000))


X_train,X_test,Y_train,Y_test = train_test_split(X,Y)


perceptron = Perceptron(epochs=100,learning_rate_b=0.000001,learning_rate_w=0.0001)
perceptron.fit(X_train,Y_train)
Y_pred = perceptron.predict(X_test)
print('Score:',perceptron.evaluate(X_test,Y_test))
