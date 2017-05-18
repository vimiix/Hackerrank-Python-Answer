from operator import itemgetter,attrgetter
students = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score])

students.sort(key=itemgetter(1,0)) #sort by score then by name 
i  = 1 
step = 0
nameList = []
while i < len(students):
    if students[i][1] != students[i-1][1]:
        step += 1
    if step == 1:
        nameList.append(students[i][0])
    if step>1:
        break
    i += 1
for i in nameList:
    print i
