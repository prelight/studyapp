import pandas as pd
import numpy as np
from datetime import datetime as dt
#rd = np.random.rand(5, 5)
#print(rd)

#標準正規分布からランダム
rdn = np.random.randn(6,4)         # 標準正規分布 (平均0, 標準偏差1)
print(rdn)

#DataFrame作成
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6,4),index = dates, columns = list("ABCD"))
print(df)
print(df.columns)
print(df.index)

#DataFrameから値取得
tstr1 = '2013-01-02'
tdatetime1 = dt.strptime(tstr1, '%Y-%m-%d')
print(df.at[tdatetime1, 'A'])
print(df.iat[0, 0])

#行指定
tstr0 = '2013-01-01'
tdatetime0 = dt.strptime(tstr0, '%Y-%m-%d')
print(df.loc[tdatetime0:tdatetime1])

#query
print(df.query('A>0 & B>0 & C>0 & D>0'))
