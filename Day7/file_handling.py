with open("hi.txt","a") as f:
    data1 = f.write("hi i am thr king")
    print(data1)

# r+ mode
with open("demo.txt","r+") as f:
    data3 = f.read()
    data3 = f.write("hi its me")
    print(data3)

# w+ mode
with open("demo.txt","w+") as f:
    data4 = f.write("hi")
    data4 = f.read()
    print(data4)




# a+ mode 
with open("demo.txt","a+") as f:
    data5 = f.write("\nhi it is again me")
    data5 = f.read()
    print(data5)