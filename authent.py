import json
import os

users_data_file_path = os.path.join('.', 'DB', 'users_data.txt')
user_session_file_path = os.path.join('.', 'DB', 'current_user.txt')


def user_register(username, email, password):
    user_data = {'username': username, 'email': email, 'password': password, 'products': []}
    user_as_json = json.dumps(user_data)
    with open(users_data_file_path, 'r+') as file:
        for each_users_data in file:
            existing_user = json.loads(each_users_data.strip())
            if existing_user['username'] == username:
                return False
        file.write(user_as_json + '\n')
        return True
