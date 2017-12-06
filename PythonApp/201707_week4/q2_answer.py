# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf

def get_answer_variable():
    a = tf.Variable(tf.zeros([2, 3]))
    #a = tf.Variable()  #これはダメ
    b = tf.Variable(tf.zeros([3, 1]))

    ans = tf.matmul(a, b)
    sess = tf.Session()

    #A = tf.constant([[1,2,3],[4,5,6]]) #これはダメ
    #B = tf.constant([[1],[2],[3]])     #これはダメ
    A = np.array([[1,2,3],[4,5,6]])
    B = np.array([[1],[2],[3]])

    sess.run(tf.global_variables_initializer())
    print(sess.run(ans, feed_dict={
        a: A,
        b: B
    }))

def get_answer_placeholder():
    a = tf.placeholder(tf.int32, shape=[2, 3])
    b = tf.placeholder(tf.int32, shape=[3, 1])

    ans = tf.matmul(a, b)
    sess = tf.Session()

    #A = tf.constant([[1,2,3],[4,5,6]]) #これはダメ
    #B = tf.constant([[1],[2],[3]])     #これはダメ
    A = np.array([[1,2,3],[4,5,6]])
    B = np.array([[1],[2],[3]])

    #sess.run(tf.global_variables_initializer()) #いらない
    print(sess.run(ans, feed_dict={
        a: A,
        b: B
    }))

def main():
    get_answer_placeholder()
    get_answer_variable()

if __name__ == '__main__':
    main()



