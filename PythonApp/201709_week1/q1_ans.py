import numpy as np
import tensorflow as tf

def main():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[1], [2], [3]])
    print(a.dot(b))

    a = tf.constant(np.array([[1, 2, 3], [4, 5, 6]]))
    b = tf.constant(np.array([[1], [2], [3]]))
    sess = tf.Session()
    print (sess.run(tf.matmul(a, b)))

if __name__ == '__main__':
    main()
