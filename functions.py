#database
#userinput
#logic

database = [
    {
        "username": "james",
        "password": "johndoe12"
    },
    {
        "username": "jude",
        "password": "jodoe133"
    },
    {
        "username": "james32",
        "password": "jdoe12"
    },
]


def check_user(username, password):
    for user in database:
        if username == user["username"] and password == user["password"]:
            return True

def login_user(username,password):
    if check_user(username,password):
        print("login successful")
    else:
        print('invalid username or password')


print('-----------Authentication---------------')

print('Input your username:')
username = input()
print('input your password:')
password = input()

login_user(username,password)
