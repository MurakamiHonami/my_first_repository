# 問題文
#N^0～N^Mの総和が10^9以下なら総和を表示
#10^9より大きい場合は文字列 inf を出力
N,M=map(int,input().split())
X=1
for m in range(1,M+1):
    X+=(N**m)
if X>10**9:
    print("inf")
else:
    print(X)