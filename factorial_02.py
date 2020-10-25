num1=input("Enter number: ")
try:
    def factorial(num): #Using Recursive Method
        if num == 0 or num ==1:
            return 1
        else:
            return num * factorial(num-1)
    print(f"Factorial of {num} is {factorial(num)}") #Recursive Method Answer
except:
    print("Please enter only integer")
