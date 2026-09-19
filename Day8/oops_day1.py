class Studen:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
s1 = Studen("daksh",97)
print(f"his name is {s1.name} and his marks is {s1.marks}%")

# creating a class and instanse
class Studen:
    name = "daksh"

s1 = Studen()
print(s1.name)
# creating instructor here this is a parametrise constructor
class Car:
    def __init__(self,brand,color,prise):  # here brand,color,prise these are paremetre
        self.company = brand
        self.looks = color
        self.cost = prise

c1 = Car("bmw","black","$5,000,000")
print(f"the brand of car is {c1.company} and color is {c1.looks} it cost around {c1.cost}")

#q1 creat a class and take 3 student and there marks of 3 subject and print the avg of the sub by method
class Student1:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3        

    def avg(self):
        avg = (self.marks1 + self.marks2 + self.marks3)/3
        return avg

st1 = Student1("daksh",99,88,99)
print(st1.avg())        

#q2 make a class of account with 2 attributes balance and account no:, the method for debit,credit,print the balance
class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
    def methods(self):
        self.credit = int(input("enter the amount for credit: "))
        self.debit = int(input("enter the amount for debit: "))
        self.balance += self.credit
        self.balance -= self.debit
        print(f"account no: {self.account_no} and the balance is {self.balance}")

p1 = Account(990000,"26-dcd-4")
p1.methods()