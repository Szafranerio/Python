# Import required modules
from collections import Counter
import numpy as np
from Decision_Tree import DecisionTree, accuracy  # Custom Decision Tree implementation and accuracy function
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Load the breast cancer dataset from scikit-learn
data = datasets.load_breast_cancer()
X = data.data        # Feature matrix
y = data.target      # Target labels

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)

# Function to create a bootstrap sample (random sampling with replacement)
def bootstrap_sample(X, y):
    n_samples = X.shape[0]
    idxs = np.random.choice(n_samples, size=n_samples, replace=True)
    return X[idxs], y[idxs]  # Return sampled features and labels

# Function to return the most common label from a list of predictions
def most_common_label(y):
    counter = Counter(y)  # Count occurrences of each label
    most_common = counter.most_common(1)[0][0]  # Return the label with the highest count
    return most_common

# Random Forest implementation using multiple Decision Trees
class RandomForest:
    def __init__(self, n_trees=100, min_samples_split=2, max_depth=100, n_feats=None):
        self.n_trees = n_trees                  # Number of trees in the forest
        self.min_samples_split = min_samples_split  # Minimum samples to split a node
        self.max_depth = max_depth              # Maximum depth of each tree
        self.n_feats = n_feats                  # Number of features to consider at each split
        self.trees = []                         # List to store trained decision trees

    # Fit the random forest model
    def fit(self, X, y):
        self.trees = []  # Reset the tree list before training
        for _ in range(self.n_trees):
            # Initialize a new decision tree with given parameters
            tree = DecisionTree(
                min_samples_split=self.min_samples_split,
                max_depth=self.max_depth,
                n_feats=self.n_feats
            )
            # Create a bootstrap sample of the training data
            X_sample, y_sample = bootstrap_sample(X, y)
            # Train the decision tree on the bootstrap sample
            tree.fit(X_sample, y_sample)
            # Add the trained tree to the forest
            self.trees.append(tree)

    # Make predictions using the random forest
    def predict(self, X):
        # Get predictions from each tree (shape: [n_trees, n_samples])
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        # Transpose to get predictions per sample (shape: [n_samples, n_trees])
        tree_preds = np.swapaxes(tree_preds, 0, 1)
        # Aggregate predictions by majority vote for each sample
        y_pred = [most_common_label(tree_pred) for tree_pred in tree_preds]
        return np.array(y_pred)

# Create and train the random forest
rf = RandomForest(n_trees=10)  # Initialize with 10 trees
rf.fit(X_train, y_train)       # Train the model

# Make predictions on the test set
rf_pred = rf.predict(X_test)

# Calculate and print the accuracy
acc = accuracy(y_test, rf_pred)
print(f'Accuracy is: {acc}')