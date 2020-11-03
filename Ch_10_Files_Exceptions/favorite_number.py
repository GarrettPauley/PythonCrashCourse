import json

def stored_num(): 
    filename = 'nums.json'
    try: 
        with open(filename) as f: 
            favorite_number = json.load(f)
    except FileNotFoundError: 
        return None
    else: 
        return favorite_number

def new_number(): 
    favorite_number = input("What is your favorite number?")
    filename = 'nums.json'

    with open(filename, 'w') as f: 
        json.dump(favorite_number, f)
    return favorite_number




def read_fav_num(): 
    favorite_number = stored_num()
    if favorite_number: 
        print(f"I remember that your favorite number is {favorite_number}")
    else: 
        favorite_number = new_number()
        print("Okay, I will remember that number!")
read_fav_num()
    