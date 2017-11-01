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
midtermGradeList = sorted([int(contentFloat[x][2]) for x in range(len(contentFloat))], reverse=True)

print("Final Grade Plot")
printStemPlot(finalGradeList)
printStatistics(finalGradeList)
print("Midterm Grade Plot")
printStemPlot(midtermGradeList)
printStatistics(midtermGradeList)
