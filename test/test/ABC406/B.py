#電卓に対して N 回操作を行う。
#N 回の操作の後に電卓に表示されている数を求める。
N,K=map(int,input().split())
A=[]
A+=list(map(int,input().split()))
result=1
for i in range(N):
    result*=A[i]#表示されている数に正の整数をかける
    if len(str(result))>=K+1:#計算結果が指定の桁数を超えたら1を表示
        result=1
print(result)