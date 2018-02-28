import pandas as pd

data = []
target = []


def get_data():
    books = ['1321-10y.xlsx']
    candles = []

    for book in books:
        excel = pd.ExcelFile(book) # bookを読む
        for sheet in excel.sheet_names:
            if sheet == '1321-10y' :
                sheetdf = excel.parse(sheet, header=None)

    #column名、定義
    cols = []
    cols.append("time")
    for i in range(10):
        cols.append("c" + str(i))
    cols.append("open")
    cols.append("high")
    cols.append("low")
    cols.append("close")
    sheetdf.columns = cols
    return sheetdf

df = get_data()


print(df["close"])


