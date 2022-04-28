from ast import While
from readline import write_history_file
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())
            
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would one wish to insert a new encryption pass or visualize existing ones (visualize, insert), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "vizualize":
        view()
    elif mode == "insert":
        add()
    else:
        print("Invalid mode.")
        continue
    
while True:
    mode = input(
        "would one wish to lock the file (lock), unlock the file (unlock), or quit (q)? ").lower()
    if mode == "q":
        breakpoint
    elif mode == "lock":
        with open('passwords.txt', 'rb') as f:
            data = f.read()
        with open('passwords.txt', 'wb') as f:
            f.write(fer.encrypt(data))
            
    elif mode == "unlock":
        write_history_file('passwords.txt')
        with open('passwords.txt', 'rb') as f:
            data = f.read()
        with open('passwords.txt', 'wb') as f:
            # decrypts the data
            f.write(fer.decrypt(data))  
    else:
        print("Invalid mode.")
        continue    
    }