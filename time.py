# hour=0
# min=0
# sec=0
s='200202'
e='240202'
# hour=int(e[:2])-int(s[:2])
# min=int(e[2:4])-int(s[2:4])
# sec=int(e[4:6])-int(s[4:6])

# total_seconds = sec + (min*60) + (hour*3600)
# print(total_seconds)

ans=0

ans1=(int(s[0:2])*3600)+(int(s[2:4])*60)+(int(s[2:6]))
ans2=(int(e[0:2])*3600)+(int(e[2:4])*60)+(int(e[2:6]))
ans=ans2-ans1
print(ans)