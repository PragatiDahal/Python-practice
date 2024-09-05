l = [11, 45, 1, 2, 4, 6, 1, 1]  
print(l)  
# l.append(7)  # Appends the value 7 to the end of the list

# l.sort() #sort the list in ascending order

# l.sort(reverse=True)  #sort the list in descending order

# l.reverse() #reverse the element of the list

# print(l.index(1))  #print the index of element 1

# print(l.count(1))  #total number of 1 present in the list

# m=l.copy() #copy the list l
# m[0]=0

# l.insert(1,899) #add 899 in the place of index1

m=[900,1000,1100]
# k=l+m
# print(k) #concatinate both the list l and m
l.extend(m) #add list m at the end of the lsit l
print(l)
