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


