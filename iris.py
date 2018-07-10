import tensorflow.contrib.learn as skflow
import tensorflow as tf
from sklearn import datasets, metrics

# 1. Collect Data
iris = datasets.load_iris()

# 2. Pick the Model
feature_columns = [tf.contrib.layers.real_valued_column("", dimension=1)]
classifier = skflow.LinearClassifier(feature_columns, n_classes=3)
# another way by implementing Deep Learning
# classifier = skflow.DNNClasssifier(feature_columns, hidden_units=[10, 20, 10], n_classes=3)

# 3. Train the Model
classifier.fit(iris.data, iris.target)

# Check the Model
score = metrics.accuracy_score(iris.target, classifier.predict(iris.data))
print("Accuracy: %f" % score)
