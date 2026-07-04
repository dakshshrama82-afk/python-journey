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