squares = [1,4,9,16,24]
print(squares)

print(squares[-1])
print(squares[1:3])
print(squares[-3:])

# assign/append values
squares[4] = 25
print(squares)

squares.append(36)
print(squares)

squares[3:4]= [1,1]
print(squares)

# initialisation 
bits = [0] * 100
print(bits)

my_list = ["a"] * 100
print(my_list)

my_list2 = [0 for _ in range(100)]
print(my_list2)

# add lists
list_1 = [1,2,3,4]
list_2 = ["a","b","c","d"]
print(list_1+list_2)

# pass by reference
list_3 = list_2
print(list_3[2]==list_3[2])