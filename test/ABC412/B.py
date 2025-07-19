#文字列S の先頭でない英大文字の直前の文字はすべて T に含まれるか判定
s=input()
t=input()
ans=True
n=len(s)
for i in range(1,n):
    if s[i].isupper():
        if s[i-1] not in t:
            ans=False
print("Yes" if ans else "No")