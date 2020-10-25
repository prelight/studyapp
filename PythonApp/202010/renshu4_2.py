# -*- coding: utf-8 -*-
from statistics import mean, median,variance,stdev

data = [71, 67, 73,61,79,59,83,87,72,79]
scores = []
for score in data:
    scores.append(score)

final_scores = [ 0.8 * i + 20 for i in scores]
print('平均点:{}'.format(median(final_scores)))
