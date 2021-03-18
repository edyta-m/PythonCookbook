usernames = ['ediscovery', 'edith-mary', 'brotherkristoph', 'edyta', 'admin']

for username in usernames:
	if username == 'admin':
		print("Hello " + username + ", would you like to see a status report?")
	else:
		print("Hello " + username + ", thank you for logging in again.")
