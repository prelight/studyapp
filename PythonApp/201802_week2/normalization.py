# -*- coding: utf-8 -*-
import numpy
import pandas
import matplotlib.pyplot as plt

from sklearn import preprocessing
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM



def main():
    data = [12,23,13,45,56];
    data = preprocessing.scale(data)
    print(data)

if __name__ == '__main__':
    main()
