import random
print ('welcomt to the guessing  coins game')
input ("press enter to start ....")
print ("1. random.raindint()")
print ("2. random.random")
choise = input (" choose the way u want to play with (1) or (2)")
if choise == "1" :
    computer = random.randint(0,1)
    if computer == 0:
       compo= "head"
    elif computer == 1:
        compo ="tail"
elif choise == "2" :
    computer = random.random()
    if computer >= 0.5:
        compo = "head"
    else :
        compo = "tail"
else :
    print ("invailed choise")
human =input ("choose a head or tail : \n")
if human == compo :
    print ("congrats u won")
else:
    print (f"bad luck u lost computer choosed {compo}")