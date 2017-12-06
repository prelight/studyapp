import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('.\mnist', one_hot=True)

x = tf.placeholder(tf.float32, [None, 784])
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, w) + b)
t = tf.placeholder(tf.float32, [None, 10])
loss = -tf.reduce_sum(t * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))
train_step = tf.train.AdamOptimizer().minimize(loss)
correct = tf.equal(tf.argmax(y, 1), tf.argmax(t, 1))
accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))

tf.summary.scalar('accuracy', accuracy)
#tf.summary.scalar('loss', loss)
merged = tf.summary.merge_all()

with tf.Session() as sess:    
    writer = tf.summary.FileWriter('.\logs', sess.graph)
    sess.run(tf.global_variables_initializer())
    for i in range(1500):
        batch = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x:batch[0], t:batch[1]})
        if not i % 100:
            summary, acc = sess.run([merged, accuracy], feed_dict={x:mnist.test.images, t:mnist.test.labels})
            #summary, acc = sess.run([merged, loss], feed_dict={x:mnist.test.images, t:mnist.test.labels})
            writer.add_summary(summary, i)
            print('Step: %d, Accuracy: %f' % (i, acc))
writer.close()
