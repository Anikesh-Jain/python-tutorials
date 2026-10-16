# Tuple are immutable so we cannot add or delete elements 

marks = (92, 94, 95, 97, 96, 95)

# lenth of the tuple
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

# check whether the value exists in tuple or not
print(95 in marks) 


# count the repeated values
print(marks.count(95))

# find the index of the paticular value
print(marks.index(97))