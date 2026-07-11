#qs1
#Print the elements of the following list using a loop:

#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

num = [1,4,9,16,25,36,49,64,81,100]
for ans in num :
    print(ans)
else:
    print("END OF LOOP")

#qs2
#Search for a number x in this tuple using loop:

#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

num = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

x = int(input("enter the no:"))
idx = 0
for y in num:
    if x == y :
        print("found the element ",x," at index:",idx)
        print("END OF LOOP")
        break
    idx += 1
else:
    print("do not exist")
    print("END OF LOOP")

# using for & range()

# 3.Print numbers from 1 to 100.

for i in range(1,101):
    print(i)
print("end of loop")


# 4.Print numbers from 100 to 1.

for i in range(100, 0, -1):
    print(i)
print("end of loop")

# 5.Print the multiplication table of a number n.
for i in range(2,21,2):
    print(i)
print("end of loop")
