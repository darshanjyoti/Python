#LIST IN PYTHON

#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary

fruits=["mango","orange","kivi","grape"]

print(type(fruits)) #<class 'list'>
print(len(fruits)) #4

print(fruits)       #['mango', 'orange', 'kivi', 'grape']
print(fruits[0])    #mango
print(fruits[0:3])  #['mango', 'orange', 'kivi']
print(fruits[-1])   #grape

#modifying list

#1. append()-> append new eleent at last
fruits.append("banana")
print(fruits)   #['mango', 'orange', 'kivi', 'grape', 'banana']

#2. insert-> insert fun is used to insert new element at specific position
fruits.insert(2,"coconut")
print(fruits)   #['mango', 'orange', 'coconut', 'kivi', 'grape', 'banana']

#3.extend->extend fun is used to insert multiple element at once
fruits2=["badam","mosombi","melon"]
fruits.extend(fruits2)
print(fruits)   #['mango', 'orange', 'coconut', 'kivi', 'grape', 'banana', 'badam', 'mosombi', 'melon']

#remove element from list
#1.pop()->pop remove the last element. It stores the removed elemnt
fruits.pop()
print(fruits)   #['mango', 'orange', 'coconut', 'kivi', 'grape', 'banana', 'badam', 'mosombi']

#2. remove()->it remove specific element
fruits.remove("banana")
print(fruits)      #['mango', 'orange', 'coconut', 'kivi', 'grape', 'badam', 'mosombi']

#reverse a list
num=[1,3,40,5,8,3,0,5]

num.reverse()
print(num)    #[5, 0, 3, 8, 5, 40, 3, 1]

#sorting a list
num.sort()
print(num)    #[0, 1, 3, 3, 5, 5, 8, 40] sort fun sort in ascending order

num.sort(reverse=True)
print(num)    #[40, 8, 5, 5, 3, 3, 1, 0]  it will sort in decending order

#note: sort() method sort the list in place. what if u dont want to sort it in place? use sorted() method
sorted_num=sorted(num)

# min max and sum
print(min(num))   #0

print(max(num))   #40

print(sum(num))   #65

#find index
print(num.index(5)) #2 FIRST OCCURENCE

#check an elemnt is in the list
print(100 in num)   #False
print("badam" in fruits)  #True


#join and split

new_fruits=' - '.join(fruits)
print(new_fruits)            #mango - orange - coconut - kivi - grape - badam - mosombi

#reverse this change
fruits3=new_fruits.split(' - ')
print(fruits3)               #['mango', 'orange', 'coconut', 'kivi', 'grape', 'badam', 'mosombi']

#Tuple : tuple are same as list but they are immutable i.e. cant be modified. written under ()

tpl=(2,4,6,7)
print(tpl)
#we can declare tuple without braket also
tppl="orange", "mango", "banana"
print(tppl)

#set -> similar to list without duplicatd

st={1,2,3,2,4}
print(st)    #{1, 2, 3, 4}

#------------------------------------------------------------------#



