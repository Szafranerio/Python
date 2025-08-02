import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
import test

bc = datasets.load_breast_cancer()
X, y = bc.data, bc.target
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=1234)

print(X_train.shape)
print(y_train.shape)

class LogisticRegression:
    def __init__(self, lr = 0.01, n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        
        
        
    def fit (self, X, y):
        n_samples, n_features = X.shape
        self.weight = np.zeros(n_features)
        self.bias = 0.0
        
        #gradient descent
        for _ in range(self.n_iters):
            linear_model = np.dot(X, self.weight) + self.bias
            y_predicted = self._sigmoid(linear_model)
            
            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            
            db = (1/n_samples) * np.sum(y_predicted - y)

            self.weight -= self.lr * dw
            self.bias -= self.lr * db
    
    def predict (self, X):
        linear_model = np.dot(X, self.weight) + self.bias
        y_predicted = self._sigmoid(linear_model)
        y_predicted_cls = [1 if i > 0.5 else 0 for i in y_predicted]
        return y_predicted_cls
    
    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
def accuracy(y_true, y_pred):
    acc = np.sum(y_true == y_pred) / len(y_true)
    return acc

reg = LogisticRegression()
reg.fit(X_train, y_train)
predictions = reg.predict(X_test)

print('LR calssification accuracy', accuracy(y_test, predictions))