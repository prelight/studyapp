# -*- coding: utf-8 -*-

import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD


# テストデータ
X = np.array([[0, 1],[1, 2],[2, 3],[3, 2],[4, 9],[5, 0],[6, 10],[7, 9],[8, 12],[9, 6],[10, 8],
              [11, 15],[12, 14],[13, 11],[14, 18],[15, 10],[16, 21],[17, 13],[18, 23],[19, 17]])
Y = np.array([[1],[1],[1],[0],[1],[0],[1],[1],[1],[0],[0],[1],[1],[0],[1],[0],[1],[0],[1],[0]])

model = Sequential()
model.add(Dense(input_dim=2, units=1))
model.add(Activation('sigmoid'))
model.compile(loss='binary_crossentropy', optimizer=SGD(lr=0.1)) #クロスエントロピー

# 学習の実行
model.ﬁt(X, Y, batch_size=1, epochs=200)

# モデルの評価
classes = model.predict_classes(np.array([[20, 19]]), batch_size=1) #クラス(カテゴリ)を返す
prob = model.predict_proba(np.array([[20, 19]]), batch_size=1)      #クラス確率を返す

print('classes=')
print(classes)
print('prob=')
print(prob)

#---------
#交差エントロピーとは損失関数の１つ
#train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)　→ 勾配降下法
#sigmoid → 活性化関数
#---------
# 疑問
# ・環境
#     pylintがkeran_envに対応していない
#     ターミナルがkeran_envになっていない
#     コマンドプロンプトをデフォルトでkeran_envの環境にしたい
# ・コード
#     batch_sizeとは？
#     input_dimって必要？　→ 検証結果：なくても行けたが・・
#     既に学習したモデルを次回使いたいときは？　→　https://ebi-works.com/keras-save/#outline__2_2


