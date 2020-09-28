even=0
userInput=int(input("Please enter a positive integer:"))
for i in range(0,userInput):
    even=i%2
    if even==0:
        print(i)

