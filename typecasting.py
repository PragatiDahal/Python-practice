# string concatenation
a="Pragati"
b="Dahal"
print(a+b)

#integer concatenation
c=5
d=10
print(c+d)

# Explicit typecasting
string="15"
number=7
string_number= int(string) #throws an error if the string is not valid integer
sum=number+string_number
print("The sum of both the numbers is:",sum)

#Implicit typecasting
p=1.9 
print(type(p))

q=9
print(type(q))

print(p+q)
print(type(p+q))