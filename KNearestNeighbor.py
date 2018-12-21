import pandas as panda
import numpy as numpy
from  sklearn import preprocessing, cross_validation, neighbors

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
dataset = panda.read_csv(url, names=names)

y = numpy.array(dataset["Class"])
X = numpy.array(dataset.drop(["Class"],axis=1))

X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size= 0.3,train_size = 0.7)

Classifier = neighbors.KNeighborsClassifier(n_neighbors=5)

Classifier.fit(X_train,y_train)

Accuracy = Classifier.score(X_test,y_test)

exp_measure = numpy.array([4.5,6.5,3.9,1.6])
exp_measure = exp_measure.reshape(1,-1)
Prediction = Classifier.predict(exp_measure)
print(Accuracy)
print(Prediction)