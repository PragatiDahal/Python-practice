def name(fname,mname,lname):
    print("Hello", fname,mname,lname)
name("James","Buchanan","Barnes")

def average(*numbers):
    print(type(numbers))  # This will print <class 'tuple'>
    sum = 0
    for i in numbers:
        sum = sum+i
    # print("Average is:", sum / len(numbers))  # Calculate and print the average
    return sum/len(numbers)

# Function call
c=average(5, 6, 7, 1)
print(c)


def name(**name):
    print(type(name))
    print("Hello", name["fname"], name["mname"], name["lname"])
name(mname="Buchanan",lname="Barnes",fname="James")

