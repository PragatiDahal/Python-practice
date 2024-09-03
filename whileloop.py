# i=0
# while (i<3):
#     print(i)
#     i= i + 1
# print("Done with the loop")

# i=int(input("Enter the number"))
# while(i<=38):
#     i=int(input("Enter the number")) #the loop takes place until and unless we give the number which is greater than 38
#     print(i)
# print("Done with the loop")

#decrementing while loop
count=5
while(count>0):
    print(count)
    count=count-1 #if we put + instead of - then infinite loop will occur
else:  #when the condition is false else is executed
    print("I am inside else")