bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])

print(bicycles[-1]) #returns the last item in array
print(bicycles[-3]) #returns the third last item in array

message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)
