import random 
print (" welcome to rock paper scissor") 
rules=  input("press enter to play or write (help) for rules :").lower()
if rules == "help":
    print( """"               ********* RULES*********
            1) You choose and the computer chooses
            2) Rock smashes Scissors -> Rock wins
            3) Scissors cut Paper -> Scissors win
            4) Paper covers Rock -> Paper wins""") 
    choice = input ("enter ur choice: \n")
    c_list = ["rock","paper","scissor"]
    pc_choice = random.choice(c_list)
    if choice  == "paper":
        print("ur choice is 🤚")
    elif choice =="scissor":
        print ("ur choice is ✌️")
    elif choice == "rock":
       print ("ur choice is 👊")
    else:
        print ("inviled choice")
if pc_choice == "paper":
    print (" computer choice is 🤚")
elif pc_choice =="scissor":
    print ("compter choice is ✌️")
elif pc_choice == "rock":
    print ("computer choice is 👊")
if pc_choice == choice :
        print ("draw")
elif choice == "paper" and  pc_choice =="rock":
        print ("congrats u won")
elif choice == "rock" and pc_choice == "scissor":
        print ("congrats u won") 
elif choice  == "scissor" and pc_choice == "paper" :
        print ("congrats u won")
elif choice == "scissor" and pc_choice == "rock":
        print ("sorry u lose")
elif choice == "paper" and pc_choice =="scissor":
        print ("sorry u lose")
elif choice == "rock" and pc_choice == "paper":
        print ("sorry u lose")
else :
        print ("")
