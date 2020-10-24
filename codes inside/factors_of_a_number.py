# Python Program to find the factors of a number

# This function computes the factor of the argument passed which is n
def print_factors(n):
   print("Factors of",n,"are : ")
   for i in range(1, n + 1):            #running a loop from 1 to n
       if n % i == 0:                      #to check if n is divisible by i
           print(i)                           #printing factors

num = int(input("enter a number: "))                    #taking input from user
print_factors(num)                   #calling function
