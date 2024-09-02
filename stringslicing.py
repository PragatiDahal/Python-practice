names="Prapti,Pragati"
print(len(names))

fruit="Mango"
mangoLen=len(fruit)
print(mangoLen)
print(fruit[0:4]) #includig 0 but not 4
print(fruit[1:4]) #including 1 but not 4
print(fruit[:5])  #inlucing 0 but not 5 , here the program automatically call value 0
print(fruit[0:])  #inlucing 0 but not 5 , here the program automatically call value 5
print(fruit[0:len(fruit)-3]) # here, it goes from 0:2 as length of fruit is 5 and 5-3 is 2
print(fruit[0:-2])           #here, it goes from 0:3 as length of fruit is 5 and 5-2 is 3
print(fruit[-1:len(fruit)-3])  #here it goes form 4:2 which does not make any sense
print(fruit[-3:-1])


nm="Harry"
print(nm[-4:-2])