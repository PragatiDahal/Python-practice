tup=(1,2,76,342,"green",True)
print(tup)
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(tup[-1])

if 342 in tup:
    print("342 is present in this tuple")
tup2=tup[1:4]
print(tup2)