import registration as reg
import attemptQuiz
import login
import completeProfile as profile


print("\n------------------------Welcome to QuizWiz------------------------\n")


while True:
    print("--> Select the number written forth to choose what you want to do\n 1. Sign Up (For New User)\n 2. Sign In\n 3. Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        reg.register()
        
    elif choice == 2:
        login.login()
        
        while login.logged_in:
            print("Select your choice ---")
            print(" 1. Attempt Quiz\n 2. Show Reults\n 3. Leaderboard\n 4. Change passsword\n 5. Change Profile\n 6. Show Profile\n 7. Log Out")
            task = int(input("Enter your choice : "))
            if task == 1:
                attemptQuiz.attempt()

            elif task == 2:
                attemptQuiz.showResults()
            elif task == 3:
                attemptQuiz.leaderboard()
            elif task == 4:
                login.changePwd()
            elif task == 5:
                profile.changeProfile()
            elif task == 6:
                profile.showProfile()
            elif task == 7:
                login.logged_in = False
                reg.logout()
            else:
                print("Invalid input")
        
    elif choice == 3:
        exit()
    else:
        print("Invalid input !!!\n")

