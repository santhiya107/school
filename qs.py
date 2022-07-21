def quicksort(a):
    less=[]
    great=[]
   
    size=len(a)
    if size<=1:
        return a
    pivot=a[0]
    for i in a[1:]:
        if pivot>i:
            less.append(i)  
        else:
            great.append(i)   
    return quicksort(less)+[pivot]+quicksort(great)
a=[6,4,78,99,389,321,1,0]
print(quicksort(a))