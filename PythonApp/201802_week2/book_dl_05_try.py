import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import SimpleRNN
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

np.random.seed(0)


def sin(x, T=100):
    return np.sin(2.0 * np.pi * x / T)


def toy_problem(T=100, ampl=0.05):
    x = np.arange(0, 2 * T + 1)
    noise = ampl * np.random.uniform(low=-1.0, high=1.0, size=len(x))
    return sin(x) + noise



def main():
    ##2次関数
    #x = np.arange(-5,5,0.01) 
    #y = x**2
    #plt.plot(y)
    ##plt.plot(x, y)
    #plt.show()

    ##ノイズ三角関数
    #T=200
    #f = toy_problem(T)
    #print(f)
    #plt.plot(f)
    #plt.show()

    #'''
    #データの生成
    #'''

    T = 100
    T = 5
    f = toy_problem(T)

    length_of_sequences = 2 * T
    maxlen = 25  # ひとつの時系列データの長さ
    maxlen = 4

    data = []
    target = []

    #print(f)
    #print(f[0:2])
    #print(f[2])

    

    for i in range(0, length_of_sequences - maxlen + 1):
        data.append(f[i: i + maxlen])
        target.append(f[i + maxlen])

    print(data)
    print('--------')
    print(target)

    X = np.array(data).reshape(len(data), maxlen, 1)
    #print(X)

    Y = np.array(target).reshape(len(data), 1)
    
    
    #続き・・
    ## データ設定
    #N_train = int(len(data) * 0.9)
    #N_validation = len(data) - N_train

    #X_train, X_validation, Y_train, Y_validation = \
    #    train_test_split(X, Y, test_size=N_validation)

    #'''
    #モデル設定
    #'''
    #n_in = len(X[0][0])  # 1
    #n_hidden = 20
    #n_out = len(Y[0])  # 1






if __name__ == '__main__':
    main()