import numpy as np
import matplotlib.pyplot as plt
import copy
import sys
import csv
import tensorflow as tf
from sklearn.utils import shuffle
from numpy.random import randn

#---------------------
##③csv
#data = [[23, 456, 67], [1,2,3]]
#ff = open('some1.csv', 'w')
#writer = csv.writer(ff, lineterminator='\n')
##writer.writerow(list)
#writer.writerows(data)
#ff.close()


#---------------------
#②concatenate
a1 = np.array([[1, 2, 3], [4, 5, 6]])
a2 = np.array([[7, 8, 9], [0, 11, 12]])

print(np.concatenate((a1, a2), axis=0))#どっちも2次元配列(1次元目が増える 行が増える)
print(np.concatenate([a1, a2], axis=0))
# [[  1  2  3]
#  [  4  5  6]
#  [  7  8  9]
#  [ 10 11 12]]

print('----')
print(np.concatenate((a1, a2), axis=1))#どっちも2次元配列(2次元目が増える 列が増える)
print(np.concatenate([a1, a2], axis=1))
# [[ 1  2  3   7  8  9]
#  [ 4  5  6  10 11 12]]
#sys.exit()



#---------------------
##①多次元スライス
#d1 = [3,5,6,6,5,8]
#d2 = [[3,5,6,6,5,8], [4,8,9,0], [1,4,7]]
#d3 = [[[3,5,6,6,5,8], [4,8,9,0], [1,4,7]],[[23, 10], [4, 67], [5, 6], [7,9]],[[1],[2]] ]

#print(d1[0:2])
#print(d2[0:2])
#print(d3[0:2])
#print("---")
#print(d1[:1])#0番目から
#print(d2[:1])#0番目から
#print(d3[:1])#0番目から
#print("---")
#print(d1[-1:])#最後の要素
#print(d2[-1:])#最後の次元
#print(d3[-1:])#最後の次元

#sys.exit()
