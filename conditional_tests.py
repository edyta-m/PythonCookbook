car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

hospital = 'Grace'
print("\nIs the hospital == 'grace'? I predict True.")
print(hospital.lower() == 'grace')

age = 28
print("\nIs my age >= 30 and age <= 40? I predict False.")
print(age >= 30 and age <= 40)

foods = ['sushi', 'tempura', 'drunken noodles', 'pizza']
print("\nIs my favourite food, drunken noodles, in the list of foods? I predict True.")
if 'drunken noodles' in foods:
	print("Drunken noodles is in the list.")
