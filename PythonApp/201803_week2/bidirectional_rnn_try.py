import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM
from keras.layers.wrappers import Bidirectional
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from sklearn import datasets
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


def getClass(val, b_val, max_val):
    sagaku = 50 / max_val
    rieki = val - b_val
    #0=ヨコヨコ,1=上がる,2=下がる

    if -sagaku <= rieki and rieki <= sagaku:
        result= [1,0,0]
    elif rieki > sagaku:
        result= [0,1,0]
    elif rieki < -sagaku:
        result= [0,0,1]
    return result

def main():
    np.random.seed(0)

    maxlen = 10 #過去10日間
    df = get_data()
    max_val = df['high'].max()
    for i in range(0, len(df) - maxlen):
        data.append(df['obs'].data[i: i + maxlen])
        cls = getClass(df['obs'].data[i + maxlen], df['obs'].data[i-1 + maxlen], max_val)
        target.append(cls)

    X = np.array(data).reshape(len(data), maxlen, 1)
    Y = np.array(target)#.reshape(len(data), 1)

    # データ設定
    N_train = int(len(data) * 0.9)
    N_test = len(data) - N_train


    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=N_test, shuffle=False)

    N_train2 = int(N_train * 0.9)
    N_validation = N_train - N_train2
    X_train, X_validation, Y_train, Y_validation = train_test_split(X_train, Y_train, test_size=N_validation)

    '''
    モデル設定
    '''
    n_in = 1
    n_time = 10
    n_hidden = 128
    n_out = 3


    def weight_variable(shape, name=None):
        return np.random.normal(scale=.01, size=shape)


    early_stopping = EarlyStopping(monitor='val_loss', patience=10, verbose=1)

    model = Sequential()
    model.add(Bidirectional(LSTM(n_hidden),
                            input_shape=(n_time, n_in)))
    model.add(Dense(n_out, kernel_initializer=weight_variable))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(lr=0.001, beta_1=0.9, beta_2=0.999),
                  metrics=['accuracy'])

    '''
    モデル学習
    '''
    epochs = 50 #300
    batch_size = 250

    hist = model.fit(X_train, Y_train,
                     batch_size=batch_size,
                     epochs=epochs,
                     validation_data=(X_validation, Y_validation),
                     callbacks=[early_stopping])

    '''
    学習の進み具合を可視化
    '''
    acc = hist.history['val_acc']
    loss = hist.history['val_loss']

    plt.rc('font', family='serif')
    fig = plt.figure()
    plt.plot(range(len(loss)), loss,
             label='loss', color='black')
    plt.xlabel('epochs')
    plt.show()


    '''
    評価
    '''
    original = []
    predicted = []
    #kakuritsu = []
    all_counter = 0
    counter = 0

    openx = df[-N_test:]['open'].data
    highx = df[-N_test:]['high'].data
    lowx = df[-N_test:]['low'].data
    closex = df[-N_test:]['close'].data


    y_ = model.predict(X_test)

    #for i in range(N_test):
    #    z_ = X_test[i:i+1]
    #    y_ = model.predict(z_)
    #    #original.append(Y_test[i])
    #    predicted.append(y_.argmax())


    write_data(predicted, "pred.csv")


    #'''
    #予測精度の評価
    #'''
    #loss_and_metrics = model.evaluate(X_test, Y_test)
    #print(loss_and_metrics)









if __name__ == '__main__':
    main()
