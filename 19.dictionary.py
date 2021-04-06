dictionary = {
	
    'a' : [1,2,3],
    'b' : 'hello',
    'c' : True
}

dictionary1 = {
	
    '123' : [1,2,3],
    True : 'hello',
    '[100]' : True
}

my_list = [
  
  
  {	
    'a' : [1,2,3],
    'b' : 'hello',
    'c' : True
  },
  {	
    'a' : [1,2,3],
    'b' : 'hello',
    'c' : True
  }
]

print(dictionary['a'])

print(dictionary)

print(my_list[0]['a'][1])

print(dictionary1['123'])

print(dictionary1[True])



user = {
	
   'name' : 'darshit',
   'basket' : [1,2,3]
}

print(user['name'])

print(user.get('age',55))

print(user)

user2 = dict(name= 'darshit')

print(user2)