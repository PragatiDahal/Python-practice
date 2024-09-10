for k in range(5):
  print(k)
  if k == 4:  
   break
else:
  print("Sorry no i") #here the program will terminate because of break


i = 0
while i<7:
  print(i)
  i = i + 1
  # if i == 4:
  #   break

else:
  print("Sorry no i") #here the whole loop will be exceuted

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")