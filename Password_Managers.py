wd = input("What is the master password?")
quit = "False"
while not quit:
    mode = input("Would you like to add new password or view exsisting one (view, add) if you want to quit choose q : \n")
    if mode == "q":
        quit = ""
    if mode == "view":
        pass 
    elif mode == "add":
        pass
    else:
        print("Invalid mode. \n")
        continue
