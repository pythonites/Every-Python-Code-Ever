#PROGRAM TO PRINT TRIANGULAR STAR PATTERN 

row = int(input("Enter number of rows: "))

for i in range(1,row+1):
	print(" "*(row-i),"*"*i)
	
'''
OUTPUT:
Enter number of rows: 10
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********

[Program finished]
	
'''

"""
Points to look for:
	1. for loop
	2. 'in' keyword
	3  range() function
"""
