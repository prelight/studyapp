import numpy as np
import matplotlib.pyplot as plt
import copy
import sys
import tensorflow as tf
from sklearn.utils import shuffle
from numpy.random import randn

#---------------------
#⑥matplotlibの描画
history = {
    'val_loss': [],
    'val_acc': []
}

fig = plt.figure()
#fig.add_subplot(3,3,5)
ax_acc = fig.add_subplot(1,1,1)
for i in range(10):
    history['val_acc'].append(i ** 2)
ax_acc.plot(range(10), history['val_acc'])
plt.show()
#ax_acc = fig.add_subplot(111)
#ran = randn(15).cumsum()
#print(ran)
# 黒色 (k) の破線で描画する
#plt.plot(ran, 'k--')



#---------------------
##⑤shuffle
#x1 = np.array(range(40))
#x1 = np.reshape(x1, (10, 4))
#x2 = np.array(range(10))
#print(x1)
#print(x2)
#print("--")
#_x1, _x2 = shuffle(x1, x2)#次元数は違ってもいいが、高次元(表現が微妙)の要素数は同じでないとダメみたい・・
#print(_x1)
#print(_x2)
#_x1, _x2 = shuffle(x1, x2)#次元数は違ってもいいが、高次元(表現が微妙)の要素数は同じでないとダメみたい・・
#print(_x1)
#print(_x2)


#---------------------
##④切り捨て除算
#x = 20
#y = 20 // 7
#print(y)


#---------------------
##③truncated_normal
#x = tf.truncated_normal(shape=[2, 5],mean=0.0, stddev=1.0,dtype=tf.float32)
#with tf.Session() as sess:
#    y = x.eval()
#    print(y)


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
#①reshapeの意味
#d1 = [3,5,6,6,5,8]
#h1 = np.array(d1).reshape(6, 1)
#print(h1)

#d2 = [[3,5,6],[6,5,8]]
#h2 = np.array(d2).reshape(2, 3, 1)
#print(h2)

#sys.exit()
