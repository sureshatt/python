import random

random_int = random.randint(1,10)
print(random_int)

random_float = random.random()
print(random_float)

random_float_range = random.uniform(4.1, 9.7)
print(random_float_range)

my_list = [1,4,5,6,7,33,57,77]
random_pick = random.choice(my_list)
print(random_pick)

# return can contain duplicates of the pupulation
choices = random.choices(my_list, k=2)
print(choices)

# returns unique elements as samples
sample = random.sample(my_list, k=3)
print(sample)

print(my_list)
random.shuffle(my_list)
print(my_list)