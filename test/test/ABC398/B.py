#7枚のカードからフルハウスが作れるか判定
A=[]
A+=list(map(int,input().split()))
cnt=0
three=False
two=False
li=[]
for a in A:
    cnt=A.count(a)
    if (cnt>=3) and (a not in li):
        three=True
        li.append(a)
        continue
    elif cnt==2:
        two=True
if (three and two) or len(li)==2:
    print("Yes")
else:
    print("No")