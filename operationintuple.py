countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)      #converting tuple into list
temp.append("Russia")       #add item at the last of the tuple
temp.pop(3)                 #remove item of index 3
temp[2] = "Finland"         #change item of index 2
countries = tuple(temp)
print(countries)

#tuples can be directly concatinated no need to change in list for concatination
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)
# res = tuple1.index(3)
# # res = tuple1.index(311)
# res = tuple1.index(3, 4, 8)
# # res = len(tuple1)
print('Count of 3 in tuple1 is:', res)