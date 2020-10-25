# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def draw_graph(q_data, kinds, expected):
    plt.rc('font', family='serif')
    plt.figure()
    # plt.ylim([0.5, 1.0])
    #plt.plot(y_test, linestyle='dashed', color='red')#実際の値
    # plt.plot(q_data, color='black')#予測値
# x = "OK" if n == 10 else "NG"
    for (dot, kind) in zip(q_data, kinds):
        x = dot[0]
        y = dot[1]
        col = 'red' if kind[0] == 0  else 'black'

        plt.plot(x, y, marker='.', color=col) 

    plt.plot(expected[0], expected[1], marker='.', color='blue') #for文の中にいれる必要あるのか？


    # plt.plot(1,1,marker='.')
    # plt.plot(1,1,color='black')
    plt.show()

def main():
    '''
    モデル学習
    '''
    # テストデータ
    X = np.array([[0, 1],[1, 2],[2, 3],[3, 2],[4, 9],[5, 0],[6, 10],[7, 9],[8, 12],[9, 6],[10, 8],
                [11, 15],[12, 14],[13, 11],[14, 18],[15, 10],[16, 21],[17, 13],[18, 23],[19, 17]])
    #Y = np.array([[0], [1], [1], [1]])
    Y = np.array([[1],[1],[1],[0],[1],[0],[1],[1],[1],[0],[0],[1],[1],[0],[1],[0],[1],[0],[1],[0]])

    Q = [20, 19]

    draw_graph(X, Y, Q)
    #get_answer_numpy()

if __name__ == '__main__':
    main()

#交差エントロピーとは損失関数の１つ
#train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)　→ 勾配降下法
#sigmoid → 活性化関数
