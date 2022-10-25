#if-else
language='python'
if(language=='python'):
	print("Yes")
else:
	print("No")   #Yes

number=2


#elif 

if(number==1):
	print('one')
elif(number==2):
	print('two')
else:
	print("three")  #two

#and or not
admin='darshan'
pw='123'
if(admin=='darshan' and pw=='123'):
	print("log in succesfull")
else:
	print("acess denied")    #log in succesfull

# == vs. is operator

a=[1,2,3]
b=[1,2,3]
print(a==b) #True
print(a is b) #False
# a is b check if the id (memory) of a and b is same or not;
c=3
d=c
print(c is d)