a= int(input("Enter any value between 5 and 9:"))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")

x=input("Enter a string:")
if(x!="quit"):
   raise ValueError("String is not quit")