# Dictonary are mutable

marks = {"Phsyics":95, "Chemistry": 96, "Maths": 98}

# insert elements with their keys
marks["English"] = 93
print(marks["English"])
print(marks)

# all values printed one by one
for key in marks:
    print(key, marks[key])

# lenth of the dictonary
print(len(marks))

# dictonary can be done empty
marks.clear()
print(marks, len(marks))