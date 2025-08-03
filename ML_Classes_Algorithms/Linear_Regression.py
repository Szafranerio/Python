import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

# Generate synthetic regression dataset
X, y = datasets.make_regression(n_samples=1000, n_features=1, noise=20, random_state=4)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# Visualize the full dataset
fig = plt.figure()
plt.scatter(X[:, 0], y, color='b', marker='o', s=30)
plt.title("Generated Data")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.show()

# Print shape of training data
print(X_train.shape)
print(y_train.shape)

# Define a custom Linear Regression model using Gradient Descent
class LinearRegression:
    def __init__(self, lr=0.1, n_iters=100):
        self.lr = lr                    # Learning rate
        self.n_iters = n_iters          # Number of training iterations
        self.weight = None              # Model weight (slope)
        self.bias = None                # Model bias (intercept)

    def fit(self, X, y):
        # Initialize parameters
        n_samples, n_features = X.shape
        self.weight = np.zeros(n_features)
        self.bias = 0.0

        # Gradient descent loop
        for _ in range(self.n_iters):
            # Linear model prediction
            y_predicted = np.dot(X, self.weight) + self.bias

            # Calculate gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # Update parameters
            self.weight -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        # Predict target values using learned parameters
        y_predicted = np.dot(X, self.weight) + self.bias
        return y_predicted

# Initialize and train the model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict on the test set
predicted = regressor.predict(X_test)

# Define Mean Squared Error function
def mse(y_true, y_predicted):
    return np.mean((y_true - y_predicted) ** 2)

# Calculate and print MSE for the test predictions
mse_value = mse(y_test, predicted)
print("Mean Squared Error:", mse_value)

# Predict on the full dataset for visualization
y_pred_line = regressor.predict(X)

# Visualize training and test points with regression line
cmap = plt.get_cmap('viridis')
fig = plt.figure()
m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10, label="Train Data")
m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10, label="Test Data")
plt.plot(X, y_pred_line, color='black', linewidth=2, label='Prediction')
plt.title("Linear Regression Fit")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.legend()
plt.show()
