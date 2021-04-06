# Tuple 

my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:4]

print(new_tuple)

x,y,z, *other = (1,2,3,4,5,6)

print(other)

my_tuple = (1,2,3,4,5,5,6,6,6)

print(my_tuple.count(5))
print(my_tuple.count(6))