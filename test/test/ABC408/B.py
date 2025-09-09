#A に含まれる数を重複を除いて小さい順に出力
N=int(input())
A=[]
A+=list(map(int,input().split()))
C=[]
for a in A:
    if a not in C:
        C.append(a)
C.sort()

print(len(C))
print(*C)