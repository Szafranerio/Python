# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

# Load the breast cancer dataset from scikit-learn
bc = datasets.load_breast_cancer()
X, y = bc.data, bc.target  # Features and target labels

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# Show the shape of the training data
print(X_train.shape)
print(y_train.shape)

# Define a custom Logistic Regression class
class LogisticRegression:
    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr                      # Learning rate
        self.n_iters = n_iters            # Number of gradient descent iterations
        self.weights = None               # Weights (parameters for features)
        self.bias = None                  # Bias (intercept)

    def fit(self, X, y):
        # Initialize weights and bias
        n_samples, n_features = X.shape
        self.weight = np.zeros(n_features)
        self.bias = 0.0

        # Perform gradient descent
        for _ in range(self.n_iters):
            # Compute linear combination of weights and input features
            linear_model = np.dot(X, self.weight) + self.bias

            # Apply sigmoid activation function to get predicted probabilities
            y_predicted = self._sigmoid(linear_model)

            # Compute gradients for weights and bias
            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1/n_samples) * np.sum(y_predicted - y)

            # Update weights and bias using gradients
            self.weight -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        # Predict using trained weights and sigmoid activation
        linear_model = np.dot(X, self.weight) + self.bias
        y_predicted = self._sigmoid(linear_model)

        # Convert probabilities into binary class labels (0 or 1)
        y_predicted_cls = [1 if i > 0.5 else 0 for i in y_predicted]
        return y_predicted_cls

    def _sigmoid(self, x):
        # Sigmoid activation function: maps values between 0 and 1
        return 1 / (1 + np.exp(-x))

# Function to calculate accuracy of predictions
def accuracy(y_true, y_pred):
    acc = np.sum(y_true == y_pred) / len(y_true)
    return acc

# Create an instance of the LogisticRegression model
reg = LogisticRegression()

# Train the model on training data
reg.fit(X_train, y_train)

# Predict on the test set
predictions = reg.predict(X_test)

# Print the classification accuracy
print('LR classification accuracy', accuracy(y_test, predictions))