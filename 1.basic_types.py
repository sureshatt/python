# basic function types

#numbers
num = 100
print(type(num))
print(isinstance(num, int))

flat_numb = 9.9
print(type(flat_numb))
print(isinstance(flat_numb, float))

comp_numb = 1 + 9j
print(type(comp_numb))
print(isinstance(comp_numb, complex))

# boolean
print(type(True))
print(isinstance(True, bool))

# chars and strings
my_string = "this is a string"
print(type(my_string))
print(isinstance(my_string, str))

my_char = 'c' # no char type in python, it is still a str
print(type(my_string))
print(isinstance(my_char, str))

#collections

# list is mutable, may contain duplicates and ordered
my_list = [1,2,3,"a", "b"]
print(type(my_list))
print(isinstance(my_list, list))

# tuple is immutable, may contain duplicates and ordered
my_tuple = (1,2,3, "a", "b")
print(type(my_tuple))
print(isinstance(my_tuple, tuple))

# set is mutable but does not allow duplicates and is not ordered
my_set = {1, 2, 3, "a", "b"} # does not allow duplicates
print(type(my_set))
print(isinstance(my_set, set)) # mutable 

my_frozenset = frozenset([1, 2, 3, "a", "b"])
print(type(my_frozenset))
print(isinstance(my_frozenset, set)) # immutable 

my_map = {"name": "bob", "age": 40}
print(type(my_map))
print(isinstance(my_map, set)) # mutable 

# binary data
my_bytes = b"hello world"
print(type(my_bytes))
print(isinstance(my_bytes, bytes))

my_byte_array = bytearray(5)
print(my_byte_array)
print(type(my_byte_array))
print(isinstance(my_byte_array, bytearray))

memory_view = memoryview(my_bytes)
print(memory_view)
print(type(memory_view))
print(isinstance(memory_view, memoryview))

# None type
x = None
print(type(x))