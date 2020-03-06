
def sort(lists):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if lists[j]<lists[minpos]:
                minpose=j
        temp=lists[i]
        lists[i]=lists[minpos]
        lists[minpos]=temp
lists=[12,2,19,976,234,675]
sort(lists)
print(lists)
