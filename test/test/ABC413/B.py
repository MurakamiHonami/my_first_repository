#N種類の文字列を連結する組み合わせは何通りあるか

N=int(input())

S=[]
for _ in range(N):      
    S+=list(input().split())
cnt=0
find=[]
for i in range(N):
    for s in S:
        if (s!=S[i]) and (s+S[i] not in find):#重複を取り除いてカウントしています
            cnt+=1
            find.append(s+S[i])
   
        
print(cnt)