import pandas as pd

titanic_df = pd.read_csv("201802_week1\\sample.csv")#ファイルパスの起点はこんな感じ
print(titanic_df.shape)

print(titanic_df.columns)

print(titanic_df['Age'])
#titanic_df
