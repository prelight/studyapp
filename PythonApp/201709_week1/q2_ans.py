import numpy as np
import tensorflow as tf

def main():
    x = tf.placeholder(tf.int32, shape=[2, 3])
    y = tf.placeholder(tf.int32, shape=[3, 1])
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[1], [2], [3]])
    sess = tf.Session()
    print(sess.run(tf.matmul(x, y), feed_dict={x:a, y: b}))


    x = tf.Variable(tf.zeros([2, 3], tf.int32))
    y = tf.Variable(tf.zeros([3, 1], tf.int32))
    up_x = x.assign(a)
    up_y = y.assign(b)
    #up_x = x.assign(tf.constant(a)) #こっちもOK
    #up_y = y.assign(tf.constant(b)) #こっちもOK
    #x = x.assign(a) #こっちもOK
    #y = y.assign(b) #こっちもOK
    
    #tf.global_variables_initializer()#いらない？
    sess = tf.Session()
    print(sess.run(tf.matmul(up_x, up_y)))
    #print(sess.run(tf.matmul(x, y))) #こっちもOK

if __name__ == '__main__':
    main()
