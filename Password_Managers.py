from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)
def add():
    name = input('Account Name: ')
    from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
quit = "False"
while not quit:
    mode = input("Would you like to add new password or view exsisting one (view, add) if you want to quit choose q : \n")
    if mode == "a":
        quit = "True"
    if mode == "view":
        pass 
    elif mode == "add":
        pass
    else:
        print("Invalid mode. \n")
        continue
quit = "False"
while not quit:
    mode = input("Would you like to add new password or view exsisting one (view, add) if you want to quit choose q : \n")
    if mode == "a":
        quit = "True"
    if mode == "view":
        pass 
    elif mode == "add":
        pass
    else:
        print("Invalid mode. \n")
        continue
quit = "False"
while not quit:
    mode = input("Would you like to add new password or view exsisting one (view, add) if you want to quit choose q : \n")
    if mode == "a":
        quit = "True"
    if mode == "view":
        pass 
    elif mode == "add":
        pass
    else:
        print("Invalid mode. \n")
        continue
