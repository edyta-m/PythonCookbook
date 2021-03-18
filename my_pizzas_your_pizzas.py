pizzas = ['Canadian', 'Buffalo Chicken', 'Tomato and Feta']

friend_pizzas = pizzas[:]

pizzas.append('Margharitta')
friend_pizzas.append('Cheese')

print("My favourite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("My friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
