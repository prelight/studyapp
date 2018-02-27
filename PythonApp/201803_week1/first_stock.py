import pandas as pd

books = ['1321-10y.xlsx']
df_list = []

for book in books:
    file = pd.ExcelFile(book) # bookを読む
    for sheet in file.sheet_names:
        df_list.append(file.parse(sheet)) # シートを順々にデータフレーム化

print(df_list[0].values)
