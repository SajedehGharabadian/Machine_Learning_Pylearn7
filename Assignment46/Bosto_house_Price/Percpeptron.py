import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
import matplotlib.animation as animation



fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(121,projection='3d')
ax1 = fig.add_subplot(122)

class Perceptron:
    def __init__(self, epochs=4, learning_rate_w=0.0001,learning_rate_b=0.01):
        self.epochs = epochs
        self.lr_w = learning_rate_w
        self.lr_b = learning_rate_b

        
    def fit(self, X, Y):
        self.W = np.random.rand(1,X.shape[1] )
        self.b = np.random.rand(1, X.shape[1])

        N = X.shape[0]
        
        fig = plt.figure(figsize=(12, 6))
        Errors = []
        
        for epoch in range(self.epochs):
            for i in range(N):
                x = X[i].reshape(-1, 1)
                y_pred = np.matmul(self.W, x) 
                e = Y[i] - y_pred 
                
                x = x.reshape(1, 2)
                self.W += self.lr_w * e * x
                self.b += self.lr_b * e

                
                fig.clear()
                ax1 = fig.add_subplot(121, projection="3d")
                ax1.clear()
                xx = np.arange(X[:, 0].min(),X[:, 0].max())
                yy = np.arange(X[:, 1].min(),X[:, 1].max())
                xx, yy = np.meshgrid(xx, yy)
                ax1.scatter(X[:, 0], X[:, 1], Y, c='green')
                Z = xx * self.W[0, 0]  + yy * self.W[0, 1]
                ax1.plot_surface(xx, yy, Z, alpha=0.5)
                ax1.set_xlabel("RM")
                ax1.set_ylabel("AGE")
                ax1.set_zlabel("Price")
                
                
                W = self.W.reshape(X.shape[1], 1)
                Y_pred = np.matmul(X, W)
                Error = np.mean(np.abs(Y - Y_pred)) 
                Errors.append(Error)
                
                
                ax2 = fig.add_subplot(122)
                ax2.clear()
                ax2.plot(Errors)
                ax2.set_title("MAE Loss")
                
                plt.pause(0.01)
    
    def predict(self,X_test):

        Y_pred = np.matmul(X_test,self.w)+self.b

        return Y_pred
    
    def evaluate(self,X_test,Y_test):
        Y_pred = self.predict(X_test)

        return mean_absolute_error(Y_test, Y_pred)
