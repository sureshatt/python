fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

# add items
fruits.append('mango')
print(fruits)

# extending with another list
fruits2 = ['tomato', 'coconut', 'coco']
fruits.extend(fruits2)
print(fruits)

# remove items
fruits.remove('kiwi') # removes the first encounter
print(fruits)

# replace itesm
print(fruits.pop(2))
print(fruits)

# clear a list
fruits2.clear()
print(fruits2)

# get index
print(fruits.index("banana"))

# count
fruits.extend(["banana, pear, kiwi"])
print(fruits.count("banana"))

# sort and reverse 
numbs = [7,5,3,6,8,4,1]
numbs.sort()
print(numbs)

numbs.reverse()
print(numbs)