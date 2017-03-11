import sqlite3
from users_queries import *

def log_users():
	username = input('Username: ')	
	password = TAKE_USER_PASSWORD
	loged_user = GET_USERNAME_AND_PASSWORD(USERNAME , PASSWORD)

	while loged_user is None:
		print('Invalid account or password! Want to continue y/n')
		user_choice = input('>')
		if user_choice == 'y' or 'Y':
			return None

		username = input('Username: ')
		password = TAKE_USER_PASSWORD
		loged_user = GET_USERNAME_AND_PASSWORD(USERNAME, PASSWORD)

	return loged_user

