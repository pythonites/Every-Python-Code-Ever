num1=input("Enter number: ")
try:
    num=int(num1)
    fact=1
    for i in range(1,num+1): #Using For Loop
        fact=fact*i
    print("Factorial of {} is {}".format(num,fact)) #For Loop Answer
except:
    print("Please enter only integer")
 
"""
Points to Ponder:
1. try-except block
2. format string (line7)
"""
