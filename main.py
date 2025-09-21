from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt




iris = datasets.load_iris()

X = iris.data  # we only take the first two features.
y = iris.target

print(X.shape)
print(y.shape)