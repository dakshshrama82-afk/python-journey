#Problem 1: Unique Elements
#Write a program that takes a list of numbers with duplicates and converts it into a set to remove duplicates.
a = int(input("enter the  no:"))
b = int(input("enter the  no:"))
c = int(input("enter the  no:"))
d = int(input("enter the  no:"))
e= int(input("enter the  no:"))
f = int(input("enter the  no:"))
g = int(input("enter the  no:"))
h = int(input("enter the  no:"))

no_set = {
    a,b,c,d,e,f,g,h
}
print(no_set)

# Problem 2: Set Operations
# Create two sets:
# A = {1, 2, 3, 4}  
# B = {3, 4, 5, 6}  
# Find and print:
# Union of A and B
# Intersection of A and B
# Difference of A and B

A = {1,2,3,4}
B ={3,4,5,6}

print(" Union :",A.union(B))
print(" Intersection:",A.intersection(B))
print("Difference:",A-B)
print("Difference:",B-A)
