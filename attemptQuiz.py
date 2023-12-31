import random
import registration as reg
import login
from datetime import datetime
from datetime import date

def attempt():
    print("Choose a technology \n")
    print("1.Python")
    print("2.Java")
    print("3.C")
    global tech
    tech = int(input("Enter your choice : "))
    i_p = input("Press enter to start the quiz")

    if(tech == 1):
        with open('pyQues.txt','r') as file:
            lines = file.readlines()
            lst = random.sample(lines, 5)
            count = 1
            score = 0
            for i in lst:
                ques = i.strip().split(', ')
                print(f"{count}. {ques[0]} \n 1.{ques[1]}\n 2.{ques[2]}\n 3.{ques[3]}\n 4.{ques[4]}")
                ans = input("Choose the correct option : ")
                if ans == ques[5]:
                    print("Correct Answer!")
                    score += 1
                else:
                    print(f"Wrong answer\nThe correct answer is option {ques[5]}")
                    # print(ques[int(ques[5])])
                count += 1
            print(f"\nYour score is : {score}")

    elif(tech == 2):
        with open('JavaQues.txt','r', encoding='utf-8') as file2:
            lines2 = file2.readlines()
            lst = random.sample(lines2, 5)
            count = 1
            score = 0
            for i in lst:
                ques = i.strip().split(', ')
                print(f"{count}. {ques[0]} \n 1.{ques[1]}\n 2.{ques[2]}\n 3.{ques[3]}\n 4.{ques[4]}")
                ans = input("Choose the correct option : ")
                if ans == ques[5]:
                    print("Correct Answer!")
                    score += 1
                else:
                    print(f"Wrong answer\nThe correct answer is option {ques[5]}")
                    # print(ques[int(ques[5])])
                count += 1
            print(f"\nYour score is : {score}")
    
    elif(tech == 3):
        with open('CQues.txt','r', encoding='utf-8') as file3:
            lines3 = file3.readlines()
            lst = random.sample(lines3, 5)
            count = 1
            score = 0
            for i in lst:
                ques = i.strip().split(', ')
                print(f"{count}. {ques[0]} \n 1.{ques[1]}\n 2.{ques[2]}\n 3.{ques[3]}\n 4.{ques[4]}")
                ans = input("Choose the correct option : ")
                if ans == ques[5]:
                    print("Correct Answer!")
                    score += 1
                else:
                    print(f"Wrong answer\nThe correct answer is option {ques[5]}")
                    # print(ques[int(ques[5])])
                count += 1
            print(f"\nYour score is : {score}")

    else:
        print("\nInvalid choice")

    with open('scores.txt', 'a') as file:
        tech_dict = {"1":"Python" , "2":"Java", "3":"C"}
        name = login.getUser()
        file.write(f"{name}, {tech_dict.get(str(tech))}, {score}, {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
def showResults():
    result_shown = False
    name = login.getUser()
    with open('scores.txt', 'r') as file:
        content = file.readlines()
        for row in content:
            data = row.strip().split(', ')
            if data[0] == name:
                result_shown = True
                print(f"Name : {data[0]}, Technology : {data[1]}, Score : {data[2]}, Date & Time : {data[3]} ")
        if result_shown == False:
            print("You haven't given any test yet!!!")    

def leaderboard():
    with open('scores.txt', 'r') as file:
        content = file.readlines()
        di = {}
        for line in content:
            data = line.strip().split(', ')
            if data[0] not in di:
                di[data[0]] = data[2]
            else:
                if int(di.get(data[0])) < int(data[2]):
                    di[data[0]] = data[2]
        leaders = sorted(di.items(), key = lambda x: int(x[1]), reverse = True)
        for name, score in leaders:
            print(f"Name : {name}, Score : {score}")




