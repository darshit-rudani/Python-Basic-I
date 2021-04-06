my_self = {
	
       'name' : 'darshit',
       'age' : 20,
       'study' : 'it engineering',
       'last name' : 'rudani'
}

your_self = {
	
       'name' : 'axay',
       'age' : 20,
       'study' : 'computer engineering'
}


print(my_self)

print('name' in my_self)

print('darshit' in my_self.values())

print('study' in my_self.keys())
print(my_self.items())
print(your_self)

your_self.clear()
print(your_self)
print(your_self.items())

my_self2 = my_self.copy()
print(my_self2)

my_self3 = your_self.copy()
print(my_self3)

my_self.pop('age')
print(my_self)

my_self.popitem()
print(my_self)

my_self.update({'age' : 30})
print(my_self)
