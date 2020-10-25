# -*- coding: utf-8 -*-
test = []
kokugo = int(input('国語：'))
test.append(kokugo)
sugaku = int(input('数学：'))
test.append(sugaku)
eigo = int(input('英語：'))
test.append(eigo)
print(test)
print('合計 {}'.format(sum(test)))
