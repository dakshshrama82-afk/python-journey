#Given an integer n, You need to use the return keyword to return twice the value of n.
n = int(input("enter the value:"))
def product(n):
    pro = n*2
    print(pro)
    return pro
product(n)

# Write a function that takes a number
# and returns both its square and cube.
a = int(input("enter the value:"))
def square_and_cube(a):
    cube = a**3
    square = a**2
    print(cube)
    print(square)
    return cube
square_and_cube(a)
# Write a function that takes a list of numbers
# and returns the largest number.
def larger_no():
    list_of_no = []
    data = True
    while data:
        a = int(input("enter the values: "))
        list_of_no.append(a)
        task = input("enter yes to stop, anything else to continue: ")
        if task == "yes":
            data = False

    largest = list_of_no[0]
    for num in list_of_no:
        if num > largest:
            largest = num
    return largest

print(larger_no())