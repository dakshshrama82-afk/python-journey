# practice quaction for while loop
#1 Print numbers from 1 to 100.

print("ans 1:")
i = 1
while i <= 100:
    print(i)
    i += 1

#2 Print numbers from 100 to 1.

print("ans 2:")
i = 100
while i >= 1:
    print(i)
    i -= 1

#3 Print the multiplication table of a number n.

print("ans 3:")
i = 1
while i<=10:
    print(17*i)
    i += 1
    

#4 Print the elements of the following list using a loop:

#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

print("ans 4:")
given_list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

i = 1
while i <= 10 :
    print(i**2)
    i += 1

#5 Search for a number x in this tuple using loop:

#[1 4 9 16 25, 36, 49, 64, 81,100]

print("ans 5:")
number = (1,4,9,16,25,36,49,64,81,100)

x = int(input("enter the value:"))
i = 0
while i < len(number):
    if x == number[i]:
        print("found at index:",i)
    elif number[i] != x:
        print("not,found",i)
    i += 1
    