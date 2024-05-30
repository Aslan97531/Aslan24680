grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(students))
a = sum(grades[0])/len(grades[0])
b = sum(grades[1])/len(grades[1])
c = sum(grades[2])/len(grades[2])
d = sum(grades[3])/len(grades[3])
e = sum(grades[4])/len(grades[4])
grades = [a, b, c, d, e]
print(grades)
print(type(grades))
students = list(students)
print(students)
students.sort()
print(students)
f = students[0]
g = students[1]
h = students[2]
i = students[3]
j = students[4]
students = [f, g, h, i, j]
print(students)
result = dict([[f,a],[g,b],[h,c],[i,d],[j,e]])
print(result)
