import numpy as np
import tensorflow as tf
import sys

'''
モデル設定
'''
tf.set_random_seed(0)  # 乱数シード

w = tf.Variable(tf.zeros([2, 1]))
b = tf.Variable(tf.zeros([1]))

x = tf.placeholder(tf.float32, shape=[None, 2])
t = tf.placeholder(tf.float32, shape=[None, 1])
y = tf.nn.sigmoid(tf.matmul(x, w) + b)

cross_entropy = - tf.reduce_sum(t * tf.log(y) + (1 - t) * tf.log(1 - y))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

correct_prediction = tf.equal(tf.to_float(tf.greater(y, 0.5)), t)


tf.summary.scalar('cross_entropy', cross_entropy)

merged = tf.summary.merge_all()

'''
モデル学習
'''
# ORゲート
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [1, 2]])
Y = np.array([[0], [1], [1], [1], [1]])

# 初期化
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

writer = tf.summary.FileWriter('./logs', sess.graph)

# 学習
for epoch in range(1000):
    if epoch % 10 == 0:
        summary, ce = sess.run([merged, cross_entropy], feed_dict={
            x: X,
            t: Y
        })
        writer.add_summary(summary, epoch)

    sess.run(train_step, feed_dict={
        x: X,
        t: Y
    })

#writer = tf.summary.FileWriter('./boad', sess.graph)


'''
学習結果の確認
'''
classified = correct_prediction.eval(session=sess, feed_dict={
    x: X,
    t: Y
})
prob = y.eval(session=sess, feed_dict={
    x: X
})

print('w:')
print(sess.run(w))
print('b:')
print(sess.run(b))

print('classified:')
print(classified)
print()
print('output probability:')
print(prob)
