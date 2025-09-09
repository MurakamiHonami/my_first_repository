#"."と"#"で構成される行列の、"."のみの行、列を圧縮する

H,W=map(int,input().split())
aw=[list(input()) for _ in range(H)]

#"."のみの行をカウントする
cnti=[]
for i in range(H):
    cnt=0
    for j in range(W):
        if aw[i][j]==".":
            cnt+=1
    if cnt==W:
        cnti.append(i)
    else:
        cnti.append([])
#"."のみの列をカウントする
cntj=[]
for j in range(W):
    cnt=0
    for i in range(H):
            if aw[i][j]==".":
                cnt+=1
    if cnt==H:
        cntj.append(j)
    else:
        cntj.append([])

#"."のみの列を削除する
if len(cntj)!=0:
        for i in range(H):
            cnt=0
            for j in cntj:
                if j!=[]:
                    j-=cnt
                    del aw[i][j]
                    cnt+=1
#"."のみの行を削除する
if len(cnti)!=0:
        cnt=0
        for j in cnti:
            if j!=[]:
                j-=cnt
                del aw[j]
                cnt+=1

#圧縮した行列を出力する
for i in aw:
    for j in i:
        print(j,end="")
    print()