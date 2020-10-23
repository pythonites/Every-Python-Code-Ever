#PROGRAM TO PRINT TRIANGULAR STAR PATTERN 

row = int(input("Enter number of rows: "))

for i in range(row,0,-1):
	print("*"*i)
	
'''
OUTPUT:
	Enter number of rows: 10
	**********
	*********
	********
	*******
	******
	*****
	****
	***
	**
	*
	
'''

"""
Points to look for:
	1. for loop
	2. 'in' keyword
	3  range() function
"""
