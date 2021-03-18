current_users = ['brotherkristoph', 'ediscovery', 'sensubean', 'chocobunny', 'jimmy']
new_users = ['ediscovery', 'brotherkristoph', 'same', 'jaws', 'ragnar']

for new_user in new_users:
	if new_user.lower() in current_users:
		print("Please enter a new username.")
	else:
		print("That username is available.")
