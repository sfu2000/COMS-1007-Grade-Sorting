import numpy as np
def printStemPlot(gradeList):
    stem = 9
    for x in reversed(range(stem)):
        line = str(x) + ' | '
        for grade in gradeList:
            if int(str(grade)[0]) == x:
                line += str(grade)[1:] + " "
        if line != str(x) + " | ":
            print(line)
def printStatistics(gradeList):
    print("Mean: " + str(np.mean(gradeList)))
    print("Standard deviation: " + str(np.std(gradeList)))

with open("grades.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]
content.pop(0)
content = [[x.split()][0] for x in content]
contentFloat = [[float(x) for x in y] for y in content]

finalGradeList = [int((contentFloat[x][0]+contentFloat[x][1]+2*contentFloat[x][2])/400*100) for x in range(len(contentFloat))]
midtermGradeList = [int(contentFloat[x][2]) for x in range(len(contentFloat))]

print("Final Grade Plot")
printStemPlot(finalGradeList)
printStatistics(finalGradeList)
print("Midterm Grade Plot")
printStemPlot(midtermGradeList)
printStatistics(midtermGradeList)


'''
Mean: 70.1136363636
Standard deviation: 12.102246052
Final Grade Plot
8 | 8 7 6 6 3 1 0 0 0 0 0 
7 | 8 7 7 6 4 4 3 3 3 3 2 2 1 1 0 0 
6 | 9 8 7 6 6 6 4 3 3 1 
5 | 9 7 7 6 3 
4 | 3 
2 | 2 
Midterm Grade Plot
8 | 1 0 1 
7 | 8 0 7 1 2 4 4 7 0 2 3 
6 | 9 6 3 1 8 9 7 2 7 5 7 0 6 1 6 
5 | 9 6 2 2 2 0 
4 | 5 5 9 5 6 7 7 3 
3 | 8 
'''
