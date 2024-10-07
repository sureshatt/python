escaped = "this is \" the way \" to do \n a second line "
print(escaped)


# raw strings do not escape \ 
raw_string = r'raw string does not escape \n or \''
print(raw_string) 

# another way to do multi lines
print(""" line1
      line2
      line3""")


# arithmatic with strings

x = 'b'
y = 'd'
z = 5*x + 2*y + 'numb'
print(z)

x = 100 * '_ok_'
print(x)

y = 'py' 'thon'
print(y)

# string as an array 
my_word = "abcdefghijklmnopqrstuvwxyz"
print(my_word[0])

# negative indices
print(my_word[-1])

#slices
print(my_word[0:3])
print(my_word[:4])
print(my_word[5:])

# strings are immutable 
my_word_2 = "this is immutable"
# my_word_2[2] = 4 will not work