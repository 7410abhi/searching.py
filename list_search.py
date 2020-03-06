L=[1,6,8,9,23]
n= int(input("enter the number you want to search: "))
"""for i in L:
    if i==n:
        print("Number found at",L[i])
        break
"""    
def search(L,n):
    i=0
    while i<len(L):
        if L[i]==n:
            print("number found at ",i)
            return True
        i=i+1
    return False
    
    
if search(L,n):
    pass
else:
    print("not found")
