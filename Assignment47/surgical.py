import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from sklearn import metrics
from Perceptron import Perceptron

df = pd.read_csv('Dataset\Surgical-deepnet.csv')

X = df.loc[:, df.columns != 'complication']
Y = df['complication']

X = np.array(X)
Y = np.array(Y)
Y = Y.reshape((Y.shape[0],1))

    
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,shuffle=True)

model = Perceptron(learning_rate=0.0001,input_length=X_train.shape[1],epochs=128)
loss_train,accuracy_train,loss_test,accuracy_test = model.fit(X_train,Y_train,X_test,Y_test)
y_pred = model.predict(X_test,Y_test)

confusion_matrix = metrics.confusion_matrix(Y_test, y_pred)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['True', 'False'])
plt.title('Confusion Matrix in test data')
cm_display.plot()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,8))

ax1.plot(accuracy_train)
ax1.plot(accuracy_test)
ax1.set_title("Accuracy")
ax1.set_xlabel("epoch")
ax1.set_ylabel("Accuracy")
ax1.legend(['train','test'])

ax2.plot(loss_train)
ax2.plot(loss_test)
ax2.set_title("Loss")
ax2.set_xlabel("epoch")
ax2.set_ylabel("Loss")
ax2.legend(['train','test'])


plt.show()