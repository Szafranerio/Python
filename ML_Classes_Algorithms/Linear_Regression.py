from cProfile import label
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
import test


X, y = datasets.make_regression(n_samples=1000, n_features=1, noise=20, random_state=4)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=1234)

fig = plt.figure()
plt.scatter(X[:, 0], y, color = 'b', marker='o', s = 30)
plt.show()

print(X_train.shape)
print(y_train.shape)

class LinearRegression:
    def __init__(self, lr = 0.1, n_iters = 100):
        self.lr = lr
        self.n_iters = n_iters
        self.weight = None
        self.bias = None
        
    def fit(self, X, y):
        # init parameters
        n_samples, n_features = X.shape
        self.weight = np.zeros(n_features)
        self.bias = 0.0
        
        # Gradient descent
        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weight) + self.bias
            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            
            db = (1/n_samples) * np.sum(y_predicted - y)

            self.weight -= self.lr * dw
            self.bias -= self.lr * db
            
    def predict(self, X):
        y_predicted = np.dot(X, self.weight) + self.bias
        return y_predicted
    
regressor = LinearRegression()
regressor.fit(X_train, y_train)
predicted = regressor.predict(X_test)

def mse(y_true, y_predicted):
    return np.mean((y_true - y_predicted)**2)

mse_value = mse(y_test, predicted)
print(mse_value)

y_pred_line = regressor.predict(X)
cmap = plt.get_cmap('viridis')
fig = plt.figure()
m1 = plt.scatter(X_train, y_train, color = cmap(0.9), s= 10)
m2 = plt.scatter(X_test, y_test, color = cmap(0.5), s = 10)
plt.plot(X, y_pred_line, color = 'black', linewidth = 2, label='Prediction')
plt.show()