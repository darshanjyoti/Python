#Dictionaries are used to store data values in key:value pairs.

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#Dictionaries are written with curly brackets, and have keys and values:

student={'name':'darshan', 'age':23, 'courses':["science",'math','computer'], 1:'example'}

print(student) #{'name': 'darshan', 'age': 23, 'courses': ['science', 'math', 'computer']}

#how to get specific value for key
print(student['name'])   #darshan

#access that is something not present
#print(student['phone']) #it will show error
#for this we can use get method
print(student.get('name'))     #darshan

print(student.get('phone'))    #None
#we can change by default none to anything.
print(student.get('phone','this key is not found'))  #this key is not found

#insert new element
student['address']='bangalore'  #{'name': 'darshan', 'age': 23, 'courses': ['science', 'math', 'computer'], 1: 'example', 'address': 'bangalore'}
print(student)

#update methode
student.update({'name':'meghna','age':19})
print(student) #{'name': 'meghna', 'age': 19, 'courses': ['science', 'math', 'computer'], 1: 'example', 'address': 'bangalore'}

#delete key
del student['age']
print(student) #{'name': 'meghna', 'courses': ['science', 'math', 'computer'], 1: 'example', 'address': 'bangalore'}
#or
age=student.pop('courses')
print(student) #{'name': 'meghna', 1: 'example', 'address': 'bangalore'}
print(age)     #['science', 'math', 'computer']


for key in student:
	print(key)      #name
                    #1
                    #address

for key,value in student.items():
	print(key,value)    #name meghna
                        #1 example
                        #address bangalore

 #---------------------------------------------#

