tasks = input ("enter the tasks for today sepprated by comma:\n ").split(", ")
complited= []
no_done = []
for dones in tasks:
    print (dones)
    comp=input("have u done this task (yes/no) \n")
    if comp == "yes":
        
        complited.append(dones)
        print ("good jop keep going")
        print ("_________")
    elif comp == ("no"):
     
        no_done.append(dones)
        print ("u better finish ur tasks today bro")
        print ('_______')
show  = input ("if u want me to show u the complited tasks js tell me : (yes/no)?")     
if show == "yes":
    print (f"here is the mission u done today : {complited}")
    print (f"here is the mission u need to done today : {no_done}")