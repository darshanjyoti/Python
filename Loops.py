# for loop

nums=[1,2,3,4]

for num in nums:
	print(num)    #1 2 3 4

#break -> it braek the loop->comes out of for loop

for num in nums:
	if(num==3):
		print('found')
		break
	print(num)   #1 2 found 

#continue->it skips the current iteration->go to next iteration

for num in nums:
	if(num==3):
		continue
	print(num)  #1 2 4

#nested loop
for num in nums:
 	for a in 'abc':
  		print(num,a)  #1 a 1 b 1 c 2 a 2 b 2 c 3 a 3 b 3 c 4 a 4 b 4 c

 #range function 

for i in range(10):
 	print(i)  #0 1 2 3 4 5 6 7 8 9

for j in range(50,56):
	print(j)  #50 51 52 53 54 55

#while loop

x=0
while(x<10):
	print(x)
	x+=1    #0 1 2 4 ....9

#---------------------------------------------------#