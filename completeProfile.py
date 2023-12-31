import registration as reg
import login
# def fillProfile():
#     print("Complete your profile before giving the quiz")
#     enrl = input("Enter your Enrollment Number : ")
#     branch = input("Enter your branch : ")
#     sem = input("Enter your semester : ")
#     with open('profile.txt','r') as file:
#         lines = file.readlines()
        
#     with open('profile.txt','w') as file:
#         for line in lines:
#             if line[0] == reg.getUser():
#                 file.write(f"{reg.getUser()}, {enrl}, {branch}, {sem}\n")
#     print("Profile completed !!!")            
        

def changeProfile():
    contact = input("Enter new mobile number : ")
    with open('profile.txt','r') as file:
        lines = file.readlines()
        
    with open('profile.txt', 'w') as file2:
        for line in lines:
            parts = line.strip().split(', ')
            if parts[0] == login.username:
                file2.write(f"{login.username}, {contact}\n")
            else:
                file2.write(line)
    print("Profile updated !!!")



def showProfile():
    print("\nYour Profile :-")
    with open('profile.txt','r') as file:
        lines = file.readlines()
        
    with open('profile.txt','r') as file:
        for line in lines:
            lst = line.strip().split(', ')
            if lst[0] == login.username:
                print("Name : " + lst[0])
                print("Mobile Number : " + lst[1])

                
