# Section 16: AI & Machine Learning with Python

## Topics

1. NumPy fundamentals
2. Pandas data manipulation
3. Matplotlib visualization
4. scikit-learn classifiers
5. TensorFlow neural networks
6. PyTorch basics
7. HuggingFace transformers
8. Ollama local AI models

## Examples

```python
# Simple classifier
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
print(f"Accuracy: {clf.score(X_test, y_test):.2%}")
```

```python
# TensorFlow model
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")
```
