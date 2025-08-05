import numpy as np
from collections import Counter
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Load the breast cancer dataset
data = datasets.load_breast_cancer()
X = data.data      # Feature matrix (inputs)
y = data.target    # Target vector (outputs: 0 = malignant, 1 = benign)

# Split data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# -------------------------------
# Function to calculate entropy
# -------------------------------
def entropy(y):
    hist = np.bincount(y)         # Count frequency of each class
    ps = hist / len(y)            # Convert counts to probabilities
    return -np.sum([p * np.log2(p) for p in ps if p > 0])  # Entropy formula

# -------------------------------
# Node class for tree structure
# -------------------------------
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature        # Index of feature to split on
        self.threshold = threshold    # Threshold value to split on
        self.left = left              # Left child
        self.right = right            # Right child
        self.value = value            # Value if it's a leaf node

    def is_leaf_node(self):
        return self.value is not None

# -------------------------------
# Main Decision Tree Classifier
# -------------------------------
class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_feats=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_feats = n_feats       # Number of features to consider at each split
        self.root = None             # Root of the tree

    def fit(self, X, y):
        # Set number of features to consider at each split
        self.n_feats = X.shape[1] if not self.n_feats else min(self.n_feats, X.shape[1])
        # Start growing the tree
        self.root = self._grow_tree(X, y)

    # Recursive method to build the tree
    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        # Check stopping conditions
        if (depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split):
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)

        # Randomly select feature indices
        feat_idxs = np.random.choice(n_features, self.n_feats, replace=False)

        # Find the best feature and threshold to split on
        best_feat, best_thresh = self._best_criteria(X, y, feat_idxs)

        # Split dataset
        left_idxs, right_idxs = self._split(X[:, best_feat], best_thresh)
        left = self._grow_tree(X[left_idxs, :], y[left_idxs], depth + 1)
        right = self._grow_tree(X[right_idxs, :], y[right_idxs], depth + 1)

        # Return current node
        return Node(best_feat, best_thresh, left, right)

    # Find the best feature and threshold for splitting
    def _best_criteria(self, X, y, feat_idxs):
        best_gain = -1
        split_idx, split_thresh = None, None

        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            thresholds = np.unique(X_column)

            for threshold in thresholds:
                gain = self._information_gain(y, X_column, threshold)

                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_thresh = threshold

        return split_idx, split_thresh

    # Calculate information gain from a potential split
    def _information_gain(self, y, X_column, split_thresh):
        parent_entropy = entropy(y)

        # Split data into left and right groups
        left_idxs, right_idxs = self._split(X_column, split_thresh)

        # If no valid split, return zero gain
        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0

        # Weighted average of child entropies
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        e_l, e_r = entropy(y[left_idxs]), entropy(y[right_idxs])
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r

        # Information gain = parent - child
        ig = parent_entropy - child_entropy
        return ig

    # Splitting data into left and right indices based on threshold
    def _split(self, X_column, split_thresh):
        left_idxs = np.argwhere(X_column <= split_thresh).flatten()
        right_idxs = np.argwhere(X_column > split_thresh).flatten()
        return left_idxs, right_idxs

    # Predict labels for a dataset
    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])

    # Traverse the tree to make a prediction
    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)

    # Return the most common label in y
    def _most_common_label(self, y):
        counter = Counter(y)
        most_common = counter.most_common(1)[0][0]
        return most_common

# -------------------------------
# Accuracy calculation function
# -------------------------------
def accuracy(y_true, y_pred):
    return np.sum(y_true == y_pred) / len(y_true)

# -------------------------------
# Training and Testing the Tree
# -------------------------------
clf = DecisionTree(max_depth=10)       # Create tree with depth limit
clf.fit(X_train, y_train)              # Train the tree
y_pred = clf.predict(X_test)           # Predict on test data
acc = accuracy(y_test, y_pred)         # Evaluate accuracy
print(f'Accuracy is {acc}')            # Print the result