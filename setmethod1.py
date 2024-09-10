# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2)) #check whether the cities or cities2 are disjoint or not

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul"}
# print(cities.issuperset(cities2)) #checks cities in superset of cities2 or not
# cities3 = {"Tokyo", "Madrid","Delhi"}
# print(cities.issuperset(cities3))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities)) #checks cities2 is subset of cities or not

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Helsinki") #add single value in set
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Helsinki", "Warsaw", "Seoul"}
# cities.update(cities2) #add more than one item 
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Tokyo") #removes item from the set
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop() #removes the item from the set but we dont know which item will be popped
# print(cities)
# print(item)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities # deletes entire set

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.clear() #delete items of the set but not entire set
# print(cities)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")



