# -*- coding: utf-8 -*-
import numpy as np
#import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def main():
    rng = np.random.RandomState(211)

    x = np.arange(20)
    t = rng.randint(-5, 6, 20)
    print(x)
    print(t)
    y = x + t
    print(y)

    for i, j, k in zip(x, y, t):
        cls = "B" if k < 0 else "A"
        print("{0} {1}".format(cls, str([i, j])))
    print("-----------")
    for i, j in zip(x, y):
        print([i, j], end=",")
    print()
    print("-----------")
    for k in t:
        cls = 0 if k < 0 else 1
        print(cls, end="],[")
    print()
    plt.scatter(x, y, marker="x", c="red", linewidth=1)
    #plt.plot([0, 20], [0, 20], c="blue")  #直線の描画
    ##plt.xlabel("x")#, fontproperties=fp)
    ##plt.ylabel("y")#, fontproperties=fp)
    plt.show()

    #----------------------------------------------------------
    #rng = np.random.RandomState(21)
    #d = 2       #次元
    #N = 10      #数
    #mean = 10
    #x1 = rng.randint(0, 10, (N, d)) + np.array([0, 0])
    #x2 = rng.randint(0, 10, (N, d)) + np.array([mean, mean])
    #print(x1)
    #print(x2)
    ##plt.plot(3,1, '.' )
    #plt.plot([3,1], '.' )
    #plt.show()

if __name__ == '__main__':
    main()
