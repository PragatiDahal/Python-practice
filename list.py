marks=[3,5,6,"Harrry",True,6,7,2,32,345,23] #list may contain different data types
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

print(marks[-3]) #Negative index
print(marks[len(marks)-3])

if 6 in marks:
    print("Yes")
else:
    print("No")

#same things for string as well
if "Ha" in "Harry":
    print("Yes")
else:
    print("No")

print(marks[1:9:3]) # here 1 is start, 9 is end and 3 is jumpcase