#直線上に並ぶN個の駅の距離を求める
N=int(input())
D=[]
D+=list(map(int,input().split()))

for i in range(1,N-1):
    D[i]+=D[i-1]
print(*D)

while len(D)>1:
    d=0
    Dis=[]
    for i in range(1,len(D)):
        d+=D[i]-D[i-1]
        Dis.append(d)
    print(*Dis)
    D=Dis[:]