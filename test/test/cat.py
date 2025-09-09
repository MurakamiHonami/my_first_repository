for i in range(1,6):
    n=5-int(i)
    print("          ",end="")
    print(" "*n,end="")
    for j in range(1,i+1):
        if j==1 or j==i:
            print("▲",end="")
        else:
            print("  ",end="")
    print(" "*n,end="")
    print(" "*n,end="")
    for j in range(1,i+1):
        if j==1 or j==i:
            print("▲",end="")
        else:
            print("  ",end="")
    print()

m=4
cnt=1
for i in range(10,15,2):
    print("    ",end="")
    for n in range(1,m):
        if cnt==1 and n==1 or cnt==2 and n==2:
            print("\ ",end="")
        else:
            print("  ",end="")
    m-=1
    for j in range(1,i+1, 1):
        if j==1 or j==i:
            print("●",end="")
        else:
            print("  ",end="")
    if cnt==1:
        print("    /",end="")
    elif cnt==2:
        print("/", end="")
    print()
    cnt+=1
print("ーーー●                        ●ーーー")
m=1
cnt=1
for i in range(14,9,-2):
    print("    ",end="")
    for n in range(1,m+1):
        if cnt==2 and n==m or cnt==3 and n==1:
            print(" /",end="")
        else:
            print("  ",end="")
    for j in range(i,0,-1):
        if j==i and i==10:
            print("● "*10,end="")
            break
        else:
            if j==1 or j==i:
                print("●",end="")
            else:
                print("  ",end="")
    for n in range(1,m+1):
        if cnt==2 and n==1 or cnt==3 and n==m:
            print("\\",end="")
        else:
            print("  ",end="")
    print()
    m+=1
    cnt+=1