import sys
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

#⑤円周上の点分布(極座標の応用、polarは不使用)
# 0〜πまでの乱数を4000個生成(一様分布)
theta = np.random.rand(4000) * np.pi 
# 2〜4までの乱数を4000個生成(正規分布)
#t = tf.truncated_normal(shape=[4000], mean=3, stddev=0.5, dtype=tf.float32)
t = tf.random_normal(shape=[4000], mean=3, stddev=0.4, dtype=tf.float32)
sess = tf.Session()
r = t.eval(session=sess)
x= r * np.cos(theta)
y= r * np.sin(theta)
plt.plot(x, y, '.')
plt.xlim([-5,5])
plt.ylim([0,8])
plt.show()



##④直線(y=50)上による点分布
#t = tf.truncated_normal(shape=[4000], mean=50, stddev=10, dtype=tf.float32)
#sess = tf.Session()
#y = t.eval(session=sess)
#x = np.random.rand(4000) * 100 - 50 # -50〜50の乱数を4000個生成
#plt.plot(x, y, '.')
#plt.xlim([-50,50])
#plt.ylim([0,100])
#plt.show()


##③切断正規分布
#x = tf.truncated_normal(shape=[4000], mean=50, stddev=10, dtype=tf.float32)
#sess = tf.Session()
#y = x.eval(session=sess)
#plt.hist(y, bins=20)     # bins本のヒストグラムを作成
#plt.show()               # グラフを表示


##②正規分布
#R = np.random.normal(50,10,4000)   # 平均50、標準偏差10の正規分布
#plt.hist(R, bins=20)     # bins本のヒストグラムを作成
#plt.show()               # グラフを表示


##①一様分布
#R = np.random.rand(1000) * 40 + 30 # 30〜70の乱数を100個生成
#plt.hist(R, bins=20)     # bins本のヒストグラムを作成
#plt.show()               # グラフを表示

