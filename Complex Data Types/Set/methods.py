marks = {98, 97, 95, 94, 96, 95, 96}

# lenth of the set
print(len(marks))

# all values printed one by one
for score in marks:
    print(score)

marks.add(92)
marks.remove(96)
print(marks)

# check whether the value exists in list or not
print(95 in marks) 

# list can be done empty
marks.clear()
print(marks, len(marks))