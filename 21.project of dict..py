#Scroll down to see the answers!
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with 
#                                                        keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value



new_game1 = {
	
	'age' : 20,
	'username' : 'Droke',
	'weapons' : ['M416' , 'AK47'],
	'is active' : 'yes',
	'clean' : 'no'
}

print(new_game1.keys())

new_game1['weapons'].append(['M24','DP28'])
print(new_game1)


new_game1.update({'is_banned' : 'false'})
print(new_game1)

new_game1['is_banned'] = 'TRUE'
print(new_game1)

game1 = new_game1.copy()
print(game1)

game1['age'] = 21
game1['username'] = 'Darshit'

print(game1)

new_game = {
	
    'age': 20,
    'username': 'droke111',
    'weapons': ['M416' , 'DP-28'],
    'is_active': 'yes',
    'clan': 'Indian'
}














print(new_game.keys())

new_game['weapons'].append(['AKM','M24'])

print(new_game)

new_game.update({'is_banned' : 'FALSE'})

print(new_game)

new_game['is_banned']='TRUE'

print(new_game)

game = new_game.copy();

print(game)

game.update({'age' : 10})

game.update({'username' : 'droke'})

print(game)