#N個の箱(B)にQ個のボールを入れる
N,Q=map(int,input().split())

X=[]
X+=list(map(int,input().split()))

B=[0 for i in range(N)]

for x in X:
    if x>0:
        print(f"{x} ",end="")
        B[x-1]=B[x-1]+1
    else:
        i=0
        for b in B:
            if b == min(B):
                break
            else:
                i+=1
        print(f"{i+1} ",end="")
        B[i]=B[i]+1
print()