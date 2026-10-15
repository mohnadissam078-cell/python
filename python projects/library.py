own =input ("enter the name of book u ahave : \n")
own2 = input ("enter another name of book u have or press enter to skip:\n")
owns = []
if own2 :
    owns.append(own)
    owns.append(own2)
    print(f"ur library is :  {owns}")
else:
    owns.append(own)
    print (F"ur library is {owns}")
wish1=input (" enter the name of book u wish u have in the future :\n")
wish2=input (" enter athe name of another book u wish u have iin the future: \n")
wishlist = []
if wish2:
    wishlist.append (wish1)
    wishlist.append (wish2)
    print (f"ur wishlist is : {wishlist}")
else:
    wishlist.append(wish1)
    print (f"ur wishlist is :{wishlist} ")
bought = input ("enter a name of book u have bought or press enter to skip:\n")
if bought :
   wishlist.remove(bought)
   owns.append(bought)
print (f"ur new library is {owns}")
print (F"ur new wishlist is {wishlist}") 
donte = input (" do u want to donate a book for poors (press enter to skip):\n" )
if donte :
    owns.remove(donte)
    print (f"now u got :{owns} in ur library")
    print (f"and u wish to get {wishlist}")
else:
    print (f"now ur library have {owns}")
    print (f"and ur wishlist is {wishlist}")
