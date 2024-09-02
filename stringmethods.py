#string are immutable
a="Pragati !!!!! Pragati"
print(len(a)) #length of a
print(a)
print(a.upper()) #print in upperclass
print(a.lower()) #print in lowerclass
print(a.rstrip("!")) #remove ! form back
print(a.replace("Pragati","Prapti")) #replace pragati with prapti
print(a.split(" ")) #seperates the list

blogHeading="introduction to PYthon" #caaptilize the I as it is the heading, only I is capital all wil be in small
print(blogHeading.capitalize())

str1="Welcome to the console!!!"
print(len(str1)) #length of the stirng
print(len(str1.center(50))) #length of the string after using center
print(str1.endswith("!!!")) #checks stirng end withs !!! or not
print(str1.endswith("to",4,10)) #checks there is "to" in between  4 and ten

print(a.count("Pragati")) #how many times pragati is used

str1="He's name is Dan.He is an honest man" #find in which index is "is"
print(str1.find("is")) 

str1="WelcomeToConsole123" #checks whether the string contains from A-Z, a-z or 0-9
print(str1.isalnum())

str1="Welcome"   #checks whether the string contains from A-Z or a-z
print(str1.isalpha())

str1="hello world"  #checks string is in lower case or not
print(str1.islower())

str1="We wish you a marry christmas" #checks string is printable or not if we use \n it is not printable
print(str1.isprintable())

str1="                             " #using space bar
print(str1.isspace())
str2="      " #using tab
print(str2.isspace())

str1="Wordl Health Organization" #checks it is title or not 
print(str1.istitle())
str2="To kill a Mocking bird"
print(str2.istitle())

str1="Python is an Interpreted language"
print(str1.startswith("Python")) #checks string starts with python or not
print(str1.swapcase()) #swaps the case convert upper to lower and vice versa

str1="His name is Dan.Dan is an honest man" #capitalize the first letter of every word
print(str1.title())