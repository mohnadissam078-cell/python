print("welcome to move the rabbit game \n")
print ("choose where u want to move the rabbit")
field = [['🌿', '🌿', '🌿'],['🌿', '🌿', '🌿'],['🌿', '🌿', '🌿']]
print (f"{field[0]} \n{field[1]} \n{field[2]}")
position = input("\nchoose the row and the column :")
row =int(position[0])
column = int (position[1])
field[row-1][column-1] = "🐇"
print ("\n success...\n")
print (f"{field[0]} \n{field[1]} \n{field[2]}")
