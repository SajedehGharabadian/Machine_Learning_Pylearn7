from random import *

def train_test_split(X,Y,test_size=0.25):
    #spilt_test = int(len(X)) * test_size
    spilt_train = int(int(len(X)) * (1-test_size))

    X_train = X[:spilt_train]
    Y_train = Y[:spilt_train]

    X_test = X[spilt_train:]
    Y_test = Y[spilt_train:]

    return X_train,X_test,Y_train,Y_test

