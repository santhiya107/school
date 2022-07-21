
#list=int([1,2,3,4,5])
#for i in list:

l1=[]
def prime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                #print(i,n//i)
                l1.append(i)
                l1.append(n//i)
                break
def check(n):
    flag = False
    if n > 1:
        for i in range(2, n):
            if (n % 2) == 0:
                flag = True
                break
    if flag == True:
        #not prime
        prime(n)
    else:
        #prime
        l.append(n)
    
    
    
   
        
        


prime(27)
print("prime factors:",l1)






            
                  
               
        
            
    
    