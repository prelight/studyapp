import sys
import numpy as np
import tensorflow as tf
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from PIL import Image

np.random.seed(0)
tf.set_random_seed(123)

##Q1
#mnist = datasets.fetch_mldata('MNIST original', data_home='.')
#print(len(mnist.data))
#print(np.shape(mnist.data))
#print(mnist.data[0])

#img1 = mnist.data[0].reshape(28, 28)
#pil_img = Image.fromarray(np.uint8(img1))
#pil_img.show()
#sys.exit()


##Q2
#rst = np.random.randint(0, 10, size=10)
#print(rst)
#rst = np.random.permutation(range(10))
#print(rst)
#sys.exit()


##Q3
#tmp = np.array([1.2, 4.5, 0.3, 1.2, 3.8, 0.8])
#rst = tmp.astype(int)
#print(rst)
#sys.exit()


##Q4
#tmp = np.array([1, 3, 1, 0, 7, 5])
#rst = np.eye(10)[tmp]
#print(rst)
#sys.exit()


##Q5
#X = np.random.permutation(range(12))
#X = X.reshape(4, 3)
#Y = np.array([True, True, True, False])
#train_size = 0.8
#print(X)
#print(Y)
#print("------------")
#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=train_size)
#print(X_train)
#print(X_test)
#print(Y_train)
#print(Y_test)
#sys.exit()


##Q6
#tmp = np.random.permutation(range(10))
#tmp = tmp.reshape(2, 5)
#b = [((i + 1) % 2) for i in tmp ]
#print(tmp)
#print(np.array(b).astype(bool))
#sys.exit()


