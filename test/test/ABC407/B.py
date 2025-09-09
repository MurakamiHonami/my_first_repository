# サイコロを 2 つ振ったときに、次の 2 つの条件の少なくとも一方を満たす確率を求める。
# 2 つの出目の合計が X 以上である。
# 2 つの出目の差の絶対値が Y 以上である。
X,Y=map(int,input().split())
total=0
rate=0
for i in range(1,7):
    for j in range(1,7):
        total+=1
        if i+j>=X:
            rate+=1
        elif abs(i-j)>=Y:
            rate+=1
if rate==0:
    print(0)
else:
    print(rate/total)