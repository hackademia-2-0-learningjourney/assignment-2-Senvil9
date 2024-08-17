import json

file_name = 'user_data.json'

def load_user_data():
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return{}

def save_user_data(data):
    with open(file_name, 'w') as f:
        json.dump(data, f)

def sign_up():
    user_data = load_user_data()

    username = input('Enter username: ')
    password = input('Enter password: ')
    mobile_number = input('mobile number: ')

    if username in user_data:
        print('username already exists!!')
    else:
        user_data[username] = {'password': password, 'mobile_number' : mobile_number}
        save_user_data(user_data)
        print('sign up successful!')

def sign_in():
    user_data = load_user_data()

    username = input('Enter username: ')
    password = input('Enter password: ')

    if username in user_data and user_data[username]['password'] == password:
        print(f'Welcome! user, Your number is {user_data[username]['mobile_number']}')
    else:
        print('Incorrect credentials.')

while True:
    print('\n1. Sign up')
    print('2. Sign in')
    choice = input('Choose an option (1 or 2): ')

    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    else:
        print('Invalid choice. Only choose 1 or 2!!')