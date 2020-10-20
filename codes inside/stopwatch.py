import time


f=input('Enter any key to start: ')
if f == 1:
	s=time.time()
else:
	s=time.time()
	


e=input('Press any key to end..')
if e==1 :
	l=time.time()
else:
	l=time.time()
	
print('time is', l-s)

import time #import the required library

#Starting the timer

start = input('Enter any key to start: ')

if start == 1:

	s = time.time() #records the time

else:

	s = time.time()

	

#stop the timer

end = input('Press any key to end..')

if end == 1 :

	l = time.time()

else:

	l = time.time()

	

print('Time is', l-s)
