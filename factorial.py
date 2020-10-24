num1=input("Enter number: ")
try:
    num=int(num1)
    fact=1
    for i in range(1,num+1): #Using For Loop
        fact=fact*i
    print("Factorial of {} is {}".format(num,fact)) #For Loop Answer

    def factorial(num): #Using Recursive Method
        if num == 0 or num ==1:
            return 1
        else:
            return num * factorial(num-1)
    print(f"Factorial of {num} is {factorial(num)}") #Recursive Method Answer
except:
    print("Please enter only integer")
