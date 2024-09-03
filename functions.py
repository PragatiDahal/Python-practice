def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("The first number is greater")
    else:
        print("The second number is greater or equal")

def isLesser(a,b): #here we can write the function later the pass will continue the program
    pass

a=8
b=9
isGreater(a,b)
calculateGmean(a,b)
#gmean1=(a*b)/(a+b)
#print(gmean1)

c=14
d=8
isGreater(c,d)
calculateGmean(c,d)
#gmean2=(c*d)/(c+d)
#print(gmean2)