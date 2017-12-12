import numpy as np
import tensorflow as tf

def main():
    #numpy
    a = np.array([[1,2,3],[4,5,6]])
    b= np.array([[1],[2],[3]])
    #b= np.array([1,2,3]) #これでもいける(下記tfはダメみたい)
    ans = np.dot(a, b)
    print(ans)

    #tf
    a = np.array([[1,2,3],[4,5,6]])
    b= np.array([[1],[2],[3]])
    #b= np.array([1,2,3]) #エラー
    ans = tf.matmul(tf.constant(a), tf.constant(b))
    #ans = tf.matmul(a, b) #これでもよい
    with tf.Session() as sess:
        print(sess.run(ans))

    print("----------------------")

    #tf(placeholder) 
    # placeholderとfeed_dictは対応している
    a = np.array([[1,2,3],[4,5,6]])
    b= np.array([[1],[2],[3]])
    x = tf.placeholder(tf.int32, shape=[2, 3]) #shapeがミソ
    y = tf.placeholder(tf.int32, shape=[3, 1])
    x_dot_y = tf.matmul(x, y)
    with tf.Session() as sess:
        y = sess.run(x_dot_y, feed_dict={x: a, y: b})
        print(y)


    #tf(変数)
    # Variableとassignは対応している
    a = np.array([[1,2,3],[4,5,6]])
    b= np.array([[1],[2],[3]])
    x = tf.Variable(tf.zeros([2, 3], tf.int32))#tf.zerosがミソ
    y = tf.Variable(tf.zeros([3, 1], tf.int32))
    with tf.Session() as sess:
        y = sess.run(tf.matmul(x.assign(a), y.assign(b)))
        print(y)



if __name__ == '__main__':
    main()
