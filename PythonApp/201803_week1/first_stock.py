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
    for i in range(10):
        cols.append("c" + str(i))
    cols.append("open")
    cols.append("high")
    cols.append("low")
    cols.append("close")
    return cols


def get_data():
    books = ['1321-10y.xlsx']
    candles = []

    for book in books:
        excel = pd.ExcelFile(book) # bookを読む
        for sheet in excel.sheet_names:
            if sheet == '1321-10y' :
                df = excel.parse(sheet, header=None)

    #column名、定義
    df.columns = get_cols_name()

    #整形
    df = df.dropna(subset=['close'])#nanを削除
    df = df.sort_values(by=['time'], ascending=True)#index 0が一番古い

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
    maxlen = 20 #過去20日間
    df = get_data()
    for i in range(0, len(df) - maxlen):
        data.append(df['close'].data[i: i + maxlen])
        target.append(df['close'].data[i + maxlen])

    #write_data(data, 'some1.csv')
    #write_data(target, 'some2.csv')

    X = np.array(data).reshape(len(data), maxlen, 1)
    Y = np.array(target).reshape(len(data), 1)

    # データ設定
    N_train = int(len(data) * 0.9)
    N_validation = len(data) - N_train

    X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=N_validation)


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
    model.add(SimpleRNN(n_hidden,
                        kernel_initializer=weight_variable,
                        input_shape=(maxlen, n_in)))
    model.add(Dense(n_out, kernel_initializer=weight_variable))
    model.add(Activation('linear'))

    optimizer = Adam(lr=0.001, beta_1=0.9, beta_2=0.999)
    model.compile(loss='mean_squared_error',
                  optimizer=optimizer,
                  metrics=['accuracy'])

    '''
    モデル学習
    '''
    epochs = 30
    batch_size = 10

    hist = model.fit(X_train, Y_train,
              batch_size=batch_size,
              epochs=epochs,
              validation_data=(X_validation, Y_validation),
              callbacks=[early_stopping])


    '''
    学習の進み具合を可視化
    '''
    val_acc = hist.history['val_acc']
    val_loss = hist.history['val_loss']

    plt.rc('font', family='serif')
    fig = plt.figure()
    #plt.plot(range(len(hist.epoch)), val_acc, label='acc', color='black')
    plt.plot(range(len(hist.epoch)), val_loss, label='acc', color='black')
    plt.xlabel('epochs')
    plt.show()


    #'''
    #予測精度の評価
    #'''
    #loss_and_metrics = model.evaluate(X_validation, Y_validation)
    #print('Test loss: %s, Test acc: %s' % (loss, acc))


    #y_ = model.predict(X_validation[:1])
    #print('---------')
    #print(X_validation[:1])
    #print('---------')
    #print(y_)


    #predict(self, x, batch_size=32, verbose=0)
    #'''
    #出力を用いて予測
    #'''
    #truncate = maxlen
    #Z = X[:1]  # 元データの最初の一部だけ切り出し

    #original = [f[i] for i in range(maxlen)]
    #predicted = [None for i in range(maxlen)]

    #for i in range(length_of_sequences - maxlen + 1):
    #    z_ = Z[-1:]
    #    y_ = model.predict(z_)
    #    sequence_ = np.concatenate(
    #        (z_.reshape(maxlen, n_in)[1:], y_),
    #        axis=0).reshape(1, maxlen, n_in)
    #    Z = np.append(Z, sequence_, axis=0)
    #    predicted.append(y_.reshape(-1))

    #'''
    #グラフで可視化
    #'''
    #plt.rc('font', family='serif')
    #plt.figure()
    #plt.ylim([-1.5, 1.5])
    #plt.plot(toy_problem(T, ampl=0), linestyle='dotted', color='#aaaaaa')
    #plt.plot(original, linestyle='dashed', color='black')
    #plt.plot(predicted, color='black')
    #plt.show()


    #print(data)
    #print('-------')
    #print(target)


if __name__ == '__main__':
    main()

#print(df["close"])


