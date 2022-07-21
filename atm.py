notes=[500,200,100]
no_in_hand=0
exist=0  
amount=int(input("enter amount"))
minamt=0
note_count=[0,0,0];

for i in notes:
    minamt+=i
    
if minamt<amount :
    for j in range(len(note_count)):  
        note_count[j]+=1
    remaining=amount-minamt
    
   
    for k in note_count:    
        no_in_hand+=k           

    for j in range(len(note_count)):   
        if remaining!=0 and remaining>=notes[j]:
            exist=remaining//notes[j] 
            remaining=remaining%notes[j]
            note_count[j]=exist+1
else:
    note=0
    temp=amount
    
    for i in range(len(notes)):
        if temp !=0 and temp>= notes[i]:
            note_count[i]=temp//notes[i]
            temp=temp-(note_count[i]*notes[i])
    
withdraw=0           
for k in note_count:    
    withdraw+=k    
print("no.of.notes.withdrawn",withdraw)

for i in range(3):        
    amount=notes[i]
    n=note_count[i]
    print('{}*{}={}'.format(amount,n,amount*n))

print(note_count)