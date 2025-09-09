# Aを末尾から削除していき、以下の条件が満たされないようにする
# 条件：A には 1 以上 M 以下の整数がすべて含まれている。
N,M=map(int,input().split())
A=[]
A+=list(map(int,input().split()))

li=[j for j in range(1,M+1)]

cnt=0
for i in range(N+1):
    for j in range(1,M+1):
        if j not in A:
            print(cnt)
            exit()
    A.pop(-1)
    cnt+=1