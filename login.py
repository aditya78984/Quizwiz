def login():
    global logged_in
    global username
    logged_in = False
    username = input("Enter username : ")
    with open('credentials.txt','r') as file:
        for i in file:
            lst = i.strip().split(', ')
            if(lst[0] == username):
                pwd = input("Enter your password : ")
                if lst[1] == pwd:
                    print("Login successfull !!")
                    logged_in = True
                else:
                    print("Wrong password !!")
        if logged_in == False:
            print("Username not found !!! Signup if you want to give the quiz")   

def getUser():
    return username


def changePwd():
    new_password = input("New Password : ")
    user = getUser()

    with open('credentials.txt', 'r') as file:
        lines = file.readlines()

    with open('credentials.txt', 'w') as file:
        for line in lines:
            parts = line.strip().split(', ')
            if parts[0] == user:
                file.write(f"{user}, {new_password}\n")
            else:
                file.write(line)             
            
        
                
