units=int(input("enter units:"))
l=[500,400,200,100]
a=[6,4,3,2]
amount=0
i=0
while(i<len(l)):
     if(units>=l[i]):        
       temp=units-l[i]
       amount+=temp*a[i]
       units=l[i];
     i+=1
amount+=units*1;   
print(amount)    