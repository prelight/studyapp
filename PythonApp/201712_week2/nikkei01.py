
#import tensorflow as tf
import keras
import numpy as np
from keras.layers import Dense, Activation
from sklearn import datasets
from sklearn.model_selection import train_test_split as split

iris = datasets.load_iris()
X_train, X_test, y_train, y_test = split(iris.data, iris.target, train_size=0.8)

model = keras.models.Sequential()
#入力層と隠れ層を指定
model.add(Dense(units=32, input_dim=4))
model.add(Activation('relu'))
model.add(Dense(units=3))
model.add(Activation('softmax')) 
model.compile(loss='sparse_categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
#学習を行う
model.fit(X_train, y_train, epochs=100)

score = model.evaluate(X_test, y_test, batch_size = 1)
print("正解率(accuracy)=", score[1])

x = np.array([[5.1, 3.5, 1.4, 0.2],[4.1, 3.5, 1.4, 1.2] ])
r = model.predict(x)
print(r)
#print(r.argmax())