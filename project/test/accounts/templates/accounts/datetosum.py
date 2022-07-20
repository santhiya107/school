def num(n):
    a=0
    while(n>0):
        a+=n%10
        n=n//10
    while(a>9):
        a=num(a)
    return(a)
name=input('Enter the string : ')
c=0
for i in name:
    c+=ord(i)
d=num(c)
print(d)