# ■Q1
# numpy、及びtensorflow(constant)を使って、それぞれ次の行列の内積ABを求めよ
# A=
# 1 2 3
# 4 5 6
# B=
# 1
# 2
# 3

import numpy as np

a = np.array([[1, 2,3],[4,5,6]])
b = np.array([1, 2, 3])

print(a.ndim)
print(a.shape)
print('----')
print(b.ndim)
print(b.shape)
print(np.dot(a,b))

print('----')
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c.ndim)
print(c.shape)
