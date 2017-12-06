import numpy as np
import tensorflow as tf
import sys

'''
モデル設定
'''
#tf.set_random_seed(0)  # 乱数シード

w = tf.Variable(tf.zeros([2, 1]))
b = tf.Variable(tf.zeros([1]))

x = tf.placeholder(tf.float32, shape=[None, 2]) # 点のデータ
t = tf.placeholder(tf.float32, shape=[None, 1]) # AかB(1か0)
y = tf.nn.sigmoid(tf.matmul(x, w) + b)

cross_entropy = - tf.reduce_sum(t * tf.log(y) + (1 - t) * tf.log(1 - y))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

#correct_prediction = tf.equal(tf.to_float(tf.greater(y, 0.5)), t)

'''
モデル学習
'''
# テストデータ
X = np.array([[0, 1],[1, 2],[2, 3],[3, 2],[4, 9],[5, 0],[6, 10],[7, 9],[8, 12],[9, 6],[10, 8],
              [11, 15],[12, 14],[13, 11],[14, 18],[15, 10],[16, 21],[17, 13],[18, 23],[19, 17]])
#Y = np.array([[0], [1], [1], [1]])
Y = np.array([[1],[1],[1],[0],[1],[0],[1],[1],[1],[0],[0],[1],[1],[0],[1],[0],[1],[0],[1],[0]])

# 初期化
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# 学習
for epoch in range(200):
    sess.run(train_step, feed_dict={
        x: X/20,
        t: Y
    })

'''
学習結果の確認
'''
print("w:")
print(sess.run(w))

#classified = correct_prediction.eval(session=sess, feed_dict={
#    x: X,
#    t: Y
#})

#test = np.array([[20, 21]])
test = np.array([[50, 51]])
#ans = np.array([[1]])
prob = y.eval(session=sess, feed_dict={
    x: test/20
})

#print('classified:')
#print(classified)
#print()
print('output probability:')
print(prob)
