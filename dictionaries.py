# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)

#accessing dictionaries items
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

#accessing multiple values
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

#accessing keys
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

#accessing key value pair
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}")