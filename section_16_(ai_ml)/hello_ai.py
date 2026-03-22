#!/usr/bin/env python3
"""Hello AI — First steps with machine learning in Python."""

import numpy as np

# Generate sample data
np.random.seed(42)
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features")
print(f"Classes: {np.unique(y)}")
print(f"Class distribution: {np.bincount(y)}")

# Simple classifier
try:
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    acc = clf.score(X_test, y_test)
    print(f"\nLogistic Regression Accuracy: {acc:.2%}")
except ImportError:
    print("\nInstall scikit-learn: pip install scikit-learn")

print("\nDone! Welcome to AI/ML with Python.")
