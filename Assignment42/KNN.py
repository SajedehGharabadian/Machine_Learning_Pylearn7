import numpy as np

class KNearest:
    def __init__(self,k):
        self.k = k
   
    #train
    def fit(self,X_train,Y_train):
        self.X_train = X_train
        self.Y_train = Y_train
        
    def euclideanDistance(self,a,b):
        d = np.sqrt(np.sum(a-b)**2)
        
        return d
    
    def nearNeighbors(self,X_test): 
        
        dists = []
        for x_train in self.X_train:
            dist = self.euclideanDistance(x_train,X_test)
            dists.append(dist)
    
        index_sorted = np.argsort(dists)
        # print(index_sorted[0:1000])
        gender_sorted = self.Y_train[index_sorted]
        return gender_sorted[0:self.k]
        
    def predict(self,X_test):
        
        neighbors = self.nearNeighbors(X_test)
        # print(neighbors)
        Y_test = np.argmax(np.bincount(neighbors))
        
        return Y_test
    
    def evaluate(self,X_test,y_test):
        test_data = []
        correct = 0
        for x_test in X_test:
            test = self.predict(x_test)
            # print(test)
            test_data.append(test)
        
        for i in range(len(X_test)):
            if test_data[i] == y_test[i]:
                correct += 1
        acc = correct/len(y_test)
                
        return acc
        

                        