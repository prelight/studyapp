import math
import numpy as np
import matplotlib.pyplot as plt

def main(): 

    # ノイズありsin関数
    ampl=0.05
    T=100
    x = np.arange(0, 2 * T + 1)#0から200までの連番
    noise = ampl * np.random.uniform(low=-1.0, high=1.0, size=len(x))#疑似乱数
    plt.plot(x, np.sin(2 * np.pi * x / T) + noise)
    plt.show()


    ## 指数関数
    #x = np.arange(0, 10, 0.1)
    #y = np.exp(x)
    #plt.plot(x, y)
    #plt.title("exponential function: $ y = e^x $")
    #plt.ylim(0, 5000)
    #plt.show()


    ## sin関数
    #pi = math.pi   #mathモジュールのπを利用
    #x = np.linspace(0, 2*pi, 100)  #0から2πまでの範囲を100分割したnumpy配列
    #y = np.sin(x)
    #plt.plot(x, y)
    #plt.show()


    ## 折れ線グラフを出力
    #left = np.array([1, 2, 3, 4, 5])
    #height = np.array([100, 300, 200, 500, 400])
    #plt.plot(left, height)
    #plt.show()

if __name__ == '__main__':
    main()
