def max_heapify(a,i):    
    l = 2*i+1
    r = 2*i+2
    if l < len(a) and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r < len(a) and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)
def max_heap(a):
    n = ((len(a)//2)-1)
    for i in range(n, -1, -1):
        max_heapify(a,i)
a = [42,50,40,55,100,10,15]
max_heap(a)
print(a)      
