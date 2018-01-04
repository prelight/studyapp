import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

def main(): 

    def sin(x, T=100):
        return np.sin(2.0 * np.pi * x / T)
 
 
    def toy_problem(T=100, ampl=0.05):
        x = np.arange(0, 2 * T + 1)
        noise = ampl * np.random.uniform(low=-1.0, high=1.0, size=len(x))
        return sin(x) + noise


    T = 100
    f = toy_problem(T)

    length_of_sequences = 2 * T # 全時系列の長さ
    maxlen = 25 # 1 つの時系列データの長さ
 
    data = []
    target = []
 
    for i in range(0, length_of_sequences - maxlen + 1):
        #print(i)
        data.append(f[i: i + maxlen])
        target.append(f[i + maxlen])
    #print(data)
    #print(maxlen)
    #print(len(data))

    #train_test_splitで使用できるようにreshape(?)
    X = np.array(data).reshape(len(data), maxlen, 1)
    Y = np.array(target).reshape(len(data), 1)

    # データ設定
    N_train = int(len(data) * 0.9)
    N_validation = len(data) - N_train
    X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=N_validation)


if __name__ == '__main__':
    main()
