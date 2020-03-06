from array import *
arr=array('i',[])  #blank array for user input
n=int(input("enter the length of an array: "))   
for i in range(n):
    x=int(input("enter the next value of an array: "))
    arr.append(x)  # this will add new element into the array
print(arr)

search=int(input("enter the no. for search: "))
'''k=0
for e in arr:
    if search==e:
        print(k)
        break'''
print(arr.index(search))   # this is a function that provides index of an element 
  
