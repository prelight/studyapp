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


data = []
target = []

def get_cols_name():
    cols = []
    cols.append("time")
    cols.append("open")
    cols.append("high")
    cols.append("low")
    cols.append("close")
    cols.append("volume")

    return cols


def get_data():
    books = ['1321-from2001.xlsx']
    candles = []

    for book in books:
        excel = pd.ExcelFile(book) # bookを読む
        for sheet in excel.sheet_names:
            if sheet == '1321-from2001' :
                df = excel.parse(sheet, header=None)

    #column名、定義
    df.columns = get_cols_name()

    #整形
    #df = df.dropna(subset=['close'])#nanを削除
    df = df.sort_values(by=['time'], ascending=True)#index 0が一番古い

    df['obs'] = df['close'] / df['close'].max()

    return df


def main():


    #3次元配列の最下行を抜き出し、要素を(例えば[8])追加して先頭(例えば[2])を削除
    a = np.array([
        [[5],[6],[7]],
        [[2],[3],[4]]
        ])
    b = [8]
    A = np.concatenate((a[-1:], [[b]]), axis=1)
    B = np.delete(A, 0, 1)
    print(B)
    sys.exit()


if __name__ == '__main__':
    main()
