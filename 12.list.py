# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list

# 2. Remove "Blueberries" from the list.

# 3. Put "Kiwi" at the end of the list.

# 4. Add "Apples" at the beginning of the list

# 5. Count how many apples in the basket

# 6. empty the basket


basket.remove('Banana')
print(basket)

basket.pop()
print(basket)

basket.insert(2,'Kiwi')
print(basket)

basket.insert(0,'Apple')
print(basket)

print(basket.count('Apple'))

print(basket)

basket.clear()

print(basket)

input('enter for exit')


basket.remove('Banana')
basket.pop()
basket.insert(2,'Kivi')
basket.insert(0,'Apples')
print(basket.count('Apples'))
print(basket)
basket.clear()
print(basket)

input('enter for exit')
