#List are mutable

marks = [92, 94, 95, 97, 96]

# lenth of the list
print(len(marks))

# indexing
print(marks[2])
print(marks[-1])

# slicing
print(marks[:])
print(marks[:3])
print(marks[2:])
print(marks[1:4])
print(marks[:-2])
print(marks[-3:])
print(marks[-3:-1])

# all values printed one by one
for score in marks:
    print(score)

# append add value in the last 
marks.append(50)
print(marks)

# add value at paticluar index
marks.insert(0, 98)
print(marks)

# check whether the value exists in list or not
print(95 in marks) 

# list can be done empty
marks.clear()
print(marks, len(marks))