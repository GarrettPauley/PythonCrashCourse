import json 

"""Load the Username, if it has been stored previously... Otherwise, prompt for the username and store it"""

def get_stored_users(): 
    filename = 'usernames.json'
    try: 
        with open(filename) as f: 
            username = json.load(f)
    except FileNotFoundError: 
        return None
    else: 
        return username

def get_new_user(): 
    username = input("what is your username?")
    filename = 'usernames.json'
    with open (filename, 'w') as f:
        json.dump(username, f)
    return username
    

def greet_user(): 
    username = get_stored_users()
    if username: 
        print(f"welcome back {username}")
    else: 
        username = get_new_user()
greet_user()



