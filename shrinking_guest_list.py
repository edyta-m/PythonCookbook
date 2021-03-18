people = ['Stephany', 'Josh', 'Vanessa', 'Kristian', 'Samantha', 'Eric', 'Miles']

print("Sorry we can only invite two guests.")

print("Sorry " + people.pop() + " you're not invited.")
print("Sorry " + people.pop() + " you're not invited.")
print("Sorry " + people.pop() + " you're not invited.")
print("Sorry " + people.pop() + " you're not invited.")
print("Sorry " + people.pop() + " you're not invited.")

print(people[0] + " you're still invited!")
print(people[1] + " you're still invited!")

del people[0]
del people[0]

print(people)
