print ("*******welcomt to the ishop calculator********")
items_number=int(input("\n how many items have u bought?: \n "))
price =[]
things= []
print ("lets go counting them.....")
for items in range (1,items_number+1):
    item_name = input(f"please tell me the name of the item number {items}:\n")
    things.append(item_name)
    item_price = float(input(f"please tell me the price of the {item_name} :\n $"))
    price.append(item_price)
price_items = (input("do u want me to show u the array of ur things and thier total price?")).lower()
if price_items =="yes":
    print(f"ur array is: {things}")
    print (f"and the total price of it is:{sum(price)}")