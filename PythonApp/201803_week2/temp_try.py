import copy
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import SimpleRNN
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle



def write_data(_data, _filename):
    ff = open(_filename, 'w')
    writer = csv.writer(ff, lineterminator='\n')
    if np.array(_data).ndim == 1:
        writer.writerow(_data)
    else:
        writer.writerows(_data)

    ff.close()


def main():
    #④1 of K 表現
    ## 3配列の2を表現
    print(np.eye(3)[2])
    ## [0,0,1]を2だと表現
    r = np.array([0,0,1])
    print(r.argmax())


    ##③mean
    #X=np.array([[2,5,4],[5,8,9]])
    #print(X)
    #print(X.mean(axis=0))#[3.5  6.5  6.5]　　(列の平均)
    #print(X.mean(axis=1))#[3.66666  7.33333] (行の平均)
    #print(len(X))#2
    #print(X.mean(axis=1).reshape(len(X), 1))#[3.66666  7.33333] (行の平均)
    #print(X - X.mean(axis=1).reshape(len(X), 1))#各行を行の平均で引いている
    ##[[-1.66666667  1.33333333  0.33333333]
    ##[-2.33333333  0.66666667  1.66666667]]
    #sys.exit()


    ##②csv逆順
    #a = [5,6,2,3,6]
    #a.reverse()
    #write_data(a, "pred.csv")
    #sys.exit()


    ##①3次元配列の最下行を抜き出し、要素を(例えば[8])追加して先頭(例えば[2])を削除
    #a = np.array([
    #    [[5],[6],[7]],
    #    [[2],[3],[4]]
    #    ])
    #b = [8]
    #A = np.concatenate((a[-1:], [[b]]), axis=1)
    #B = np.delete(A, 0, 1)
    #print(B)
    #sys.exit()


if __name__ == '__main__':
    main()
