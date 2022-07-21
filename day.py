start='20000718'
end='20020230'
l=[]
day=(int(end[6:])-int(start[6:]))
month=(int(end[4:6])-int(start[4:6]))
year=(int(end[:4])-int(start[:4]))
for i in range(1,int(year)):
l.append(int(start[:4])+i)

print(l)





for i in range(1, 8): 

for j in range(1, i + 1): 
if(i%2 == 0) :
pass
else: 
print("* ", end="") 
print() 
