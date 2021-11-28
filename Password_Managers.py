from cryptography.fernet import Fernet
wd = input("What is the master password?")
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key()
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())
key = load_key()
fer = Fernet(key)
quit = "False"
while not quit:
    mode = input("Would you like to add new password or view exsisting one (view, add) if you want to quit choose q : \n")
    if mode == "q":
        quit = "True"
    if mode == "view":
        pass 
    elif mode == "add":
        pass
    else:
        print("Invalid mode. \n")
        continue
