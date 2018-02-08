import numpy as np
import matplotlib.pyplot as plt
import copy
import sys
import tensorflow as tf



#---------------------
#①reshapeの意味
#d1 = [3,5,6,6,5,8]
#h1 = np.array(d1).reshape(6, 1)
#print(h1)

#d2 = [[3,5,6],[6,5,8]]
#h2 = np.array(d2).reshape(2, 3, 1)
#print(h2)

#sys.exit()

#---------------------
##②参照渡し
#a = np.arange(0, 12)
##a = range(0, 12)
##b = np.reshape(copy.copy(a), (3, 4)) # 3×4の２次元配列に変形。
#b = np.reshape(a, (3, 4)) # 3×4の２次元配列に変形。
#b[2, 2] = 99
#print(a)
#print(b)

#---------------------
#③truncated_normal
x = tf.truncated_normal(shape=[2, 5],mean=0.0, stddev=1.0,dtype=tf.float32)
with tf.Session() as sess:
    y = x.eval()
    print(y)
