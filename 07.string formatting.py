# 1 What would be the output of the below 4 print statements? 

print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

# 2 How would you write this using f-string? 

name = 'Cindy'
amount = 50

print(f"Hello {name}, your balance is {amount}.")


