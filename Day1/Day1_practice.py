# Day 1 phython practice
# Problem 1: Greeting with Input,Ask the user for their name and age, then print:Hello <name>, you are <age> years old!
print("Hello my name is aman sir,what is your name")
name = input("enter the nmae:")
print("sir",name,"what is your age")
age = int(input("enter the age:"))
print("Hello sir ",name,", you are",age,"years old!")

#Problem 2: Simple Calculator,Ask the user for two numbers and print their sum, difference, product, and quotient.
no_1 = int(input("enter the first no:"))
no_2 = int(input("enter the 2nd no:"))

sum = no_1 +no_2
difference = no_1 - no_2
product = no_1 * no_2
if no_2 == 0:
    print("division by zero is not possible")
else:
    quotient = no_1/no_2

print("answer sheet:")         
print("sum=",sum)
print("difference=",difference)
print("product=",product)
print("quotient=",quotient)

#Problem 3: Even or Odd

a = int(input("enter the no"))

if a%2 == int:
    print("the no was even")
else:
    print("the no was odd")


