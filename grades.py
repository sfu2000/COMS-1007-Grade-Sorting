with open("grades.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]
content.pop(0)
gradeList = [(int(x[0:2])+int(x[5:7])+2*int(x[-2:])) for x in content]
gradeList = [float(x)/400 for x in gradeList]
gradeList = [x*100 for x in gradeList]

import numpy as np
np.std(gradeList)
np.mean(gradeList)

stem = 8

for x in gradeList:
    first = int(str(x)[0])
    if first == stem:
        line = ' | '
        for y in gradeList:
            if str(y)[0] == str(first):
                line += str(int(y))[1:] + ' '
        print(str(stem) + line)
        stem -= 1

'''
Result =
8 | 8 7 6 6 3 1 0 0 0 0 0
7 | 8 7 7 6 4 4 3 3 3 3 2 2 1 1 0 0
6 | 9 8 7 6 6 6 4 3 3 1
5 | 9 7 7 6 3
4 | 3
'''
