def register():
    with open('credentials.txt','a') as file:
        global username
        username = input("Enter your name : ")
        pwd = input("Set a password : ")
        contact = input("Enter your phone number : ")
        file.write(f"{username}, {pwd}\n")
        file2 = open('profile.txt', 'a')
        file2.write(f"{username}, {contact}\n")
        file2.close()
    print(f"Registration done , {username} , remember your password: {pwd}\n")
        
        
        

def getUser():
    return username
            
  


# Add the following line to ensure the file exists before attempting to change the password.

def logout():
    print("Logged Out Successfully")
    exit()

        



'''
file2 = open('credentials.txt', 'r+')

for i in file2:
    lst = i.strip().split(', ')
    print(lst)

'''



