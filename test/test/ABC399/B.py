# 問題文
# 1 から  N までの番号が付けられた  N 人の人がとあるコンテストに参加し、人  i (1≤i≤N) の 得点 は P iでした。
# このコンテストでは、以下の手順によって  N 人それぞれの 順位 が定まります。
# 変数  r を用意し、 r=1 と初期化する。最初、 N 人の順位はすべて未確定である。
# N 人全員の順位が確定するまで以下の操作を繰り返す。
# 順位が未確定である人の中での得点の最大値を  x とし、得点が  x である人の数を  k とおく。得点が  x である 
# k 人すべての順位を  r 位と確定させたのち、 r に  k を足す。
# N 人それぞれの順位を出力してください。
N=int(input())
P=[]
P+=list(map(int,input().split()))
r=1

rank=[[] for _ in range(N)]
while r<N+1:
    x=max(P)
    k=P.count(x)
    i=-1
    for _ in range(k):
        i=P.index(x,i+1)
        rank[i]=r
        P[i]=-1
    r+=k
for ra in rank:
    print(ra)