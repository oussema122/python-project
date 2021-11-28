pwd = input("What is the master password?")
quit = "True"
while not quit:
    mode = input("Would you like to add new password or view exsisting one (view, add) if you want to quit choose q")
    if mode == "q":
        quit = "False"
    if mode == "view":
        pass 
    elif mode == "add":
        pass
    else:
        print("Invalid mode.")
        continue
        
