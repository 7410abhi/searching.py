from numpy import *
L=[9,10,13,76,99,123,762,888,981]
n=99
def search(L,n):
    lw=0
    upp=len(L)-1
    while lw<=upp:
        mid=(upp+lw)//2
        if L[mid]==n:
            globals()['pos']=mid
            return True
        else:
          if L[mid]<n:
              lw=mid
          elif L[mid]>n:
              upp=mid
if search(L,n):
    print("number found at",pos+1)
else:
    print("not found")
      

      
