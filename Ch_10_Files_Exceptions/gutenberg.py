

def common_words(files): 

    try: 
        with open(files, encoding='utf-8') as f:
            content = f.read()

    except FileNotFoundError: 
        print(f"could not find {files}")
    
    else: 
        find = input('What word would you like to search for? ' )
        num = content.lower().count(find)
        print(f"{files} contains {num} instances of {find} ")

files = ['Dr. Hyde.txt', 'Alice.txt', 'Moby.txt']
for file in files: 
    common_words(file)
    

  
    
