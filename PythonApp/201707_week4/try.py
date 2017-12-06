# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf

def main():
    a = tf.zeros([2,1])
    #a = tf.zeros([1])
    sess = tf.Session()
    print(sess.run(a))


    #n = 5
    #Y1 = np.array([[1, 0, 0] for i in range(n)])
    #Y2 = np.array([[0, 1, 0] for i in range(n)])
    #Y3 = np.array([[0, 0, 1] for i in range(n)])
    #Z1 = np.array([1, 0, 0])
    #print(Y1)
    #print(Y2)
    #print(Y3)
    #print(Z1)


if __name__ == '__main__':
    main()



