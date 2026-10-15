print ("welcome to the multiplication \n")
number = int (input("enter the number u want the multiplication table of : \n"))
print ("ur multiplication taple is: ")
for multi in range(1,11):
    print (f"{number} * {multi} =  {multi * number}") 
