import numpy as np
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt 


class Perceptron:
    def __init__(self, epochs=4, learning_rate_w=0.0001,learning_rate_b=0.01):
        self.epochs = epochs
        self.lr_w = learning_rate_w
        self.lr_b = learning_rate_b

        
    def fit(self, X, Y):
        self.w = np.random.rand(1,X.shape[1] )
        self.b = np.random.rand(1, X.shape[1])

        N = X.shape[0]
        
        Errors = []
        
        for epoch in range(self.epochs):
            for i in range(N):
                x = X[i].reshape(-1,1)
                
                y_pred = x @ self.w +self.b
                e = Y[i] - y_pred # just 1 Error
                
                
                self.w = self.w + (self.lr_w * e * x)
                self.b = self.b +(self.lr_b * e)
                                
                self.w = self.w.reshape(X.shape[1], 1)
                Y_pred = np.matmul(X,self.w)
                Error = np.mean(np.abs(Y - Y_pred)) 
                Errors.append(Error)

        


        plt.figure(figsize=(6, 6))
        plt.scatter(X,Y,c='blue')
        plt.plot(X,Y_pred,color="red")
        plt.show()  
                
                
            
    def predict(self,X_test):

        Y_pred = np.matmul(X_test,self.w)+self.b

        return Y_pred
    
    def evaluate(self,X_test,Y_test):
        Y_pred = self.predict(X_test)

        return mean_absolute_error(Y_test, Y_pred)
