dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#won't allow the following because dimensions is a tuple, meaning the array contents are immutable
#dimensions[0] = 250

print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
