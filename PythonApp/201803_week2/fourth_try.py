
import os
import copy
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import GRU
from keras.layers.recurrent import LSTM
from keras.layers.recurrent import SimpleRNN
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle


data = []
target = []
#openx = []
#highx = []
#lowx = []

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

    df['obs'] = df['close'] / df['high'].max()

    #df['openx'] = df['open'] / df['high'].max()
    #df['highx'] = df['high'] / df['high'].max()
    #df['lowx'] = df['low'] / df['high'].max()

    return df


def write_data(_data, _filename):
    ff = open(_filename, 'w')
    writer = csv.writer(ff, lineterminator='\n')
    if np.array(_data).ndim == 1:
        writer.writerow(_data)
    else:
        writer.writerows(_data)

    ff.close()


def main():
    maxlen = 10 #過去10日間
    df = get_data()
    max_val = df['high'].max()
    for i in range(0, len(df) - maxlen):
        data.append(df['obs'].data[i: i + maxlen])
        ##if 
        #sa = (df['obs'].data[i + maxlen] - df['obs'].data[i + maxlen - 1])/df['obs'].data[i + maxlen - 1]
        #if sa > 0.01:
        #    val = 1
        #elif sa < 0.01:
        #    val = -1
        #else:
        #    val = 0
        ##target.append( 1 if df['close'].data[i + maxlen] >= 0.01 else 0 )
        #target.append(val)
        target.append(df['obs'].data[i + maxlen])


    #write_data(data, 'some1.csv')
    #write_data(target, 'some2.csv')

    X = np.array(data).reshape(len(data), maxlen, 1)
    Y = np.array(target).reshape(len(data), 1)

    # データ設定
    N_train = int(len(data) * 0.9)
    #N_validation = len(data) - N_train
    N_test = len(data) - N_train


    #X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=N_validation)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=N_test, shuffle=False)


    N_train2 = int(N_train * 0.9)
    N_validation = N_train - N_train2
    X_train, X_validation, Y_train, Y_validation = train_test_split(X_train, Y_train, test_size=N_validation)


    '''
    モデル設定
    '''
    n_in = len(X[0][0])  # 1
    n_hidden = 30
    n_out = len(Y[0])  # 1


    def weight_variable(shape, name=None):
        return np.random.normal(scale=.01, size=shape)


    early_stopping = EarlyStopping(monitor='val_loss', patience=10, verbose=1)
    model = Sequential()
    model.add(GRU(n_hidden,
                    kernel_initializer=weight_variable,
                    input_shape=(maxlen, n_in)))
    #model.add(LSTM(n_hidden,
    #            kernel_initializer=weight_variable,
    #            input_shape=(maxlen, n_in)))

    model.add(Dense(n_out, kernel_initializer=weight_variable))
    model.add(Activation('linear'))

    optimizer = Adam(lr=0.001, beta_1=0.9, beta_2=0.999)
    model.compile(loss='mean_squared_error',
                    optimizer=optimizer,
                    metrics=['accuracy'])


    path = 'param.hdf5'
    if os.path.exists(path) :
        model.load_weights(path)
    else:

        '''
        モデル学習
        '''
        epochs = 30 #あとで30に戻そう！！
        batch_size = 10

        hist = model.fit(X_train, Y_train,
                  batch_size=batch_size,
                  epochs=epochs,
                  validation_data=(X_validation, Y_validation),
                  callbacks=[early_stopping])

        model.save_weights(path)

        #'''
        #学習の進み具合を可視化
        #'''
        val_acc = hist.history['val_acc']
        val_loss = hist.history['val_loss']

        plt.rc('font', family='serif')
        fig = plt.figure()
        #plt.plot(range(len(hist.epoch)), val_acc, label='acc', color='black')
        plt.plot(range(len(hist.epoch)), val_loss, label='loss', color='black')
        plt.xlabel('epochs')
        plt.show()


    #'''
    #予測精度の評価
    #'''
    #loss_and_metrics = model.evaluate(X_validation, Y_validation)
    #print('Test loss: %s, Test acc: %s' % (loss, acc))

    ##最新予測
    #new = np.concatenate((X_test[-1:], [Y_test[-1:]]), axis=1)
    #new = np.delete(new, 0, 1)
    #y_ = model.predict(new)
    #print('---------')
    #print(new)
    #print('---------')
    #print(y_)


    ##predict(self, x, batch_size=32, verbose=0)

    #---------------------------------------------------------

    original = []
    predicted = []
    #kakuritsu = []
    all_counter = 0
    counter = 0

    openx = df[-N_test:]['open'].data
    highx = df[-N_test:]['high'].data
    lowx = df[-N_test:]['low'].data
    closex = df[-N_test:]['close'].data

    for i in range(N_test):
        z_ = X_test[i:i+1]
        y_ = model.predict(z_)
        original.append(Y_test[i])
        predicted.append(y_.argmax())

        #if len(original) > 1:
        #    if (closex[i-1] - openx[i-1] > 0):
        #        all_counter += 1
        #        if (original[len(original)-1] - original[len(original)-2] > 0) and \
        #           (predicted[len(predicted)-1] - predicted[len(predicted)-2] > 0):
        #            counter += 1
        #    elif  (closex[i-1] - openx[i-1] < 0):
        #        all_counter += 1
        #        if (original[len(original)-1] - original[len(original)-2] < 0) and \
        #           (predicted[len(predicted)-1] - predicted[len(predicted)-2] < 0):
        #            counter += 1

        #high = highx[i]
        #low = lowx[i]
        #val = y_[0][0] * max_val
        #if low < val and val < high:
        #    counter += 1

    #print( counter / (N_test-1))
    #print( counter / all_counter)




    #'''
    #グラフで可視化
    #'''
    plt.rc('font', family='serif')
    plt.figure()
    #plt.ylim([0.5, 1.0])
    #plt.plot(toy_problem(T, ampl=0), linestyle='dotted', color='#aaaaaa')
    plt.plot(original, linestyle='dashed', color='red')
    plt.plot(predicted, color='black')
    plt.show()


    predicted.reverse()
    write_data(predicted, "pred.csv")

    #print(data)
    #print('-------')
    #print(target)


if __name__ == '__main__':
    main()

#print(df["close"])


