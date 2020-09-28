userInput=int(input("Please enter an integer bigger or equal to 1:"))
for i in range (0,userInput+1):
    print((userInput-i) * ' ' + i * '*')
