ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2) #updates the item of ep1
# ep1.clear() #delete the item from the dicitionaries
# ep1.pop(122) #pop the item 122:45
ep1.popitem() #pop the last item i.e 670:69
del ep1[122] #delete 122:45 from dictionaries
print(ep1) 