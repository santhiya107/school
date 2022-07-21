def heapify(a, l, i):     
    max = i 
    lc = 2 * i + 1 
    rc = 2 * i + 2     
    if (lc < l and a[lc] > a[max]):
        max = lc    
    if (rc < l and a[rc] > a[max]):
        max = rc    
    if (max != i):
        a[i],a[max]=a[max],a[i]          
        heapify(a,l,max)

a= [42,50,40,55,100,10,15 ] 
l= len(a)
#delete(a)
print(a)

        