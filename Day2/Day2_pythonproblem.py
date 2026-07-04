#Problem: Traffic Light Simulator
#Write a Python program that takes the current traffic light color as input (red, yellow, or green) and prints the action a driver should take.

light = input("enter the color of light")

if light == "red":
    print("stop.Wait until green.")
elif light == "yellow":
    print("Slow down.")
elif light == "green":
    print("go.")
else:
    print("light is broken.")

#Problem 1: Café Menu Order
#Write a program that asks the user to choose an item (pizza, burger, or coffee) and prints the price.

#Requirements:

#If the choice is "pizza", print "Price: ₹250".

#If "burger", print "pice: ₹120".

#If "coffee", print "Price: ₹80".

#Otherwise, print "Item not available".

print("welcome to the cafe")
menu = {
    "pizza" : "₹250",
    "burger" : "₹120",
    "coffee" : "₹80"
}
print(menu)
order = input("choose the item from the menu")
if "pizza" == order:
    print("Price: ₹250")
elif "burger"== order:
    print("price: ₹120")
elif "coffee"== order:
    print("Price: ₹80")
else:
    print("Item not available")

#Problem 3: Café Order with Quantity
#Write a program that asks the user to choose an item (pizza, burger, or coffee) and also enter the quantity. Then calculate and print the total bill.

#Requirements:

#If the choice is "pizza", price = ₹250 × quantity.

#If "burger", price = ₹120 × quantity.

#If "coffee", price = ₹80 × quantity.

#Otherwise, print "Item not available".



print("welcome to the cafe")
menu = {
    "pizza" :  250,
    "burger" :  120,
    "coffee" :  80
}
print(menu)
order = input("choose the item from the menu")
quantity = int(input("enter the quantity"))
if "pizza" == order:
    print("Price: ₹250 x ",quantity)
    print("Total Bill: ₹",menu[order]*quantity)
elif "burger"== order:
    print("price: ₹120 x ",quantity)
    print("Total Bill: ₹",menu[order]*quantity)
elif "coffee"== order:
    print("Price: ₹80 x ",quantity)
    print("Total Bill: ₹",menu[order]*quantity)
else:
    print("Item not available")
