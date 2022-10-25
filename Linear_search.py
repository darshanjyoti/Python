def search(list,k):
	for i in range(len(list)):
		if(list[i]==k):
			print("key is present")
			break
	else:
		print("key is not present")

list1=[1,2,3,4,5]
key=8
search(list1,key)

#or 
def search(list,k):
	for i in list:
		if(i==k):
			print("key is present")
			break
	else:
		print("key is not present")

list1=[1,2,3,4,5]
key=8
search(list1,key)



