# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf


def get_answer_numpy():
    a = np.array([[1,2,3],[4,5,6]])
    b = np.array([[1],[2],[3]]) #どっちでもOK
    #b = np.array([1, 2, 3])    #どっちでもOK
    
    ans = a.dot(b)
    print(ans)
    

def get_answer_tensorflow():
    a = tf.constant([[1,2,3],[4,5,6]])
    b = tf.constant([[1],[2],[3]])  #こちらはOK
    #b = tf.constant([1,2,3])       #こちらはダメ
    ans = tf.matmul(a, b)
    sess = tf.Session()
    print(sess.run(ans))


def main():
    get_answer_numpy()
    get_answer_tensorflow()

if __name__ == '__main__':
    main()



