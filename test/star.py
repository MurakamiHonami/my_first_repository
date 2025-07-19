# ループを使って星を書きます

for i in range(1,6):
    print(" "*9,end="")
    for j in range(1,6-i):
        print(" ",end="")
    for j in range(1,i):
        print("★ ",end="")
    print()
for i in range(4,0,-1):
    for j in range(1,5-i):
        print("  ",end="")
    for j in range(1,i+1):
        print("★ ",end="")
    for j in range(1,7):
        print("★ ",end="")
    for j in range(1,i+1):
        print("★ ",end="")
    print()

for i in range(5,0,-1):
    for j in range(1,i-1):
        print("  ",end="")
    for j in range(1,i):
        print("★ ",end="")
    for j in range(1,6-i):
        print(" "*j,end="")
    for j in range(1,6-i):
        print("  ",end="")
    for j in range(1,6-i):
        print("   ",end="")
    for j in range(1,i):
        print("★ ",end="")
    print()